class AuthenticationPageLocators():

    email_locator = [
        ("id", "email"),
        ("xpath", "//input[@placeholder='email']")
    ]

    password_locator = [
        ("id", "password"),
        ("name", "password"),
        ("xpath", "//input[@type='password']")
    ]

    name_locator = [
        ("id", "name"),

    ]

    loginbutton_locator = [
        ("id", "auth-login-button"),
        ("name", "auth-login-button"),
        ("css", "#auth-login-button")
    ]

    signupbutton_locator = [
        ("id", "auth-login-button"),
    ]


    switch_auth_mode_locator = [
        ("id", "switch-auth-mode"),
    ]

    login_error_locator = [
        ("class_name", "modal__content"),
    ]

    error_okay_locator = [
        ("name", "Ham"),
    ]
