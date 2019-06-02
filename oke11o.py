from config import users
from instapy import InstaPy
from instapy import smart_run
from instapy import click_element
from instapy import sleep
from instapy import web_address_navigator
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
import random


def watch_the_story(browser, logger):

    # TODO: See (def like_image(browser, username, blacklist, logger, logfolder))
    # TODO:
    #  Открываем тэг
    #  Кликаем по аватарке тэга и попадаем на экран сторис
    #  Спим 1 сек и кликаем дальше вперед
    user_link = "https://www.instagram.com/stories/kirill.toros/"
    # check URL of the webpage, if it already is user's profile page,
    # then do not navigate to it again
    web_address_navigator(browser, user_link)



    like_xpath = "//section/span/button/span[@aria-label='Like']"
    unlike_xpath = "//section/span/button/span[@aria-label='Unlike']"

    # find first for like element
    like_elem = browser.find_elements_by_xpath(like_xpath)


    # xpaths
    prev_xpath = "//button/div[@class='coreSpriteRightChevron']"
    next_xpath = "//button/div[@class='coreSpriteRightChevron']"
    close_xpath = "//button/div[@class='coreSpriteCloseLight']"
    prev_elem = None
    next_elem = None
    try:
        # check if there is a story for this user according to IG user data
        is_story = browser.execute_script(
            "return window._sharedData.entry_data.StoriesPage[0].user.id")
        print(is_story)
        is_story = True
        if is_story:
            # first img is a story
            first_imag = browser.find_element_by_tag_name("img")
            click_element(browser, first_imag)
            sleep(2)
            # find the buttons before story ends to save time on xpath fail
            close_elem = browser.find_element_by_xpath(close_xpath)
            while random.randint(1,5) != 1:
                # find the element
                if next_elem is None:
                    next_elem = browser.find_element_by_xpath(next_xpath)
                sleep(random.randint(2,6))
                # move to the right (next)
                click_element(browser, next_elem)
                sleep(2) # let the prev button load
                if random.randint(1, 10) == 1:
                    if prev_elem is None:
                        prev_elem = browser.find_element_by_xpath(prev_xpath)
                    sleep(random.randint(2, 4))
                    # play with it, we can go back
                    click_element(browser, prev_elem)
            sleep(5)
            # close button since this is a long story..
            click_element(browser, close_elem)
    except NoSuchElementException:
        # story is finished
        pass
    except StaleElementReferenceException:
        # story is finished
        pass
    except WebDriverException:
        logger.error('has_highlight_reel not exist')
    except:
        logger.error('Story: something went wrong')

insta_username = users['oke11o']['login']
insta_password = users['oke11o']['pass']

# get an InstaPy session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    # session.set_dont_include(["friend1", "friend2", "friend3"])

    # session.set_relationship_bounds(enabled=True,
    #                                 potency_ratio=-1.0,
    #                                 delimit_by_numbers=True,
    #                                 max_followers=4590,
    #                                 max_following=5555,
    #                                 min_followers=1,
    #                                 min_following=1)

    # session.set_do_comment(True, percentage=10)
    # session.set_comments(['amazing!', 'So much fun!!', 'Nicey!', 'Cool!!', 'Awesome!'])


    # watch_the_story(session.browser, session.logger)
    # activity
    session.like_by_tags([
        'coding',
        # 'russia',
        # 'programming',
        # 'developer',
        # 'travel',
        # 'trip',
        # 'it',
        # 'symfony',
        # 'travel',
        # 'trip',
        # 'relax',
        # 'rest',
        # 'happy',
        # 'счастье',
        # 'москва',
        # 'программирование',
        # 'отдых'
    ], amount=2)
    print("DONE")


