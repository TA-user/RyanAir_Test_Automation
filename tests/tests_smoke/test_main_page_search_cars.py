def test_user_can_hire_car(browser, main_page, main_page_car_hire_tab):
    main_page.open()
    main_page.click_accept_cookie_popup_button()
    main_page.open_search_cars_tab()
    main_page_car_hire_tab.perform_car_sharing("Berlin", "2022-04-10", "10:00", "2022-04-11", "10:00")
