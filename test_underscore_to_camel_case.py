import camel_case as cc
import nose.tools as nt


def test_underscore_to_camel_case():
    result = cc.underscore_to_camel_case("some_test_data")
    nt.eq_("someTestData", result)


def test_sequential_underscores():
    result = cc.underscore_to_camel_case("some__test_____data")
    nt.eq_("someTestData", result)


def test_keep_upper_case():
    result = cc.underscore_to_camel_case("output_HTML_view",
                                         keep_upper_case=True)
    nt.eq_("outputHTMLView", result)


def test_ends_with_underscore():
    result = cc.underscore_to_camel_case("test_data_")
    nt.eq_("testData", result)


def test_starts_with_underscore():
    result = cc.underscore_to_camel_case("_hello_world")
    nt.eq_("helloWorld", result)


def test_starts_with_underscore_first_capital():
    result = cc.underscore_to_camel_case("_hello_world",
                                         start_with_capital=True)
    nt.eq_("HelloWorld", result)


def test_lower_case_no_underscores():
    result = cc.underscore_to_camel_case("test")
    nt.eq_("test", result)


def test_start_capital():
    result = cc.underscore_to_camel_case("test", start_with_capital=True)
    nt.eq_("Test", result)