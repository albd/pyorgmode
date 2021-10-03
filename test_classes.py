from datetime import date, datetime
from .pyorgmode import OrgDate, OrgFile, OrgHeading, OrgLink, OrgString
import pytest

@pytest.fixture
def org_file():
    return OrgFile()

def test_date():
    od = OrgDate(datetime(2021, 10, 2, 18, 32))
    assert(str(od) == '[2021-10-02 Sat 18:32]')

def test_link():
    ol = OrgLink(title='Orgmode homepage', url='https://orgmode.org/')
    assert(str(ol) == "[[https://orgmode.org/][Orgmode homepage]]")

def test_org_string():

    # test simple string
    os = OrgString("hello world")
    assert(str(os) == "hello world")

    # test string containing date and link
    os = OrgString([
        OrgDate(datetime(2021, 10, 2, 18, 32)),
        " today todos ",
        OrgLink(title='Orgmode homepage', url='https://orgmode.org/'),
    ])
    assert(str(os) == '[2021-10-02 Sat 18:32] today todos [[https://orgmode.org/][Orgmode homepage]]')

def test_heading():

    # floating org heading not added to any file
    heading = OrgHeading(heading="hello world")
    assert(str(heading) == "* hello world")

    # heading with tags
    heading = OrgHeading(heading="hello world", tags=['blue', 'red'])
    assert(str(heading) == "* hello world :blue:red:")

    # heading with body
    heading = OrgHeading(heading="hello world", body="Where is everybody?")
    assert(str(heading) == "* hello world\nWhere is everybody?")

    # heading with orgstring
    heading = OrgHeading(heading=OrgString([
        OrgDate(datetime(2021, 10, 2, 18, 32)),
        " hello world"
        ]))
    assert(str(heading) == "* [2021-10-02 Sat 18:32] hello world")

    # heading with orgstring, body and tags
    heading = OrgHeading(
        heading=OrgString([
            OrgDate(datetime(2021, 10, 2, 18, 32)),
            " hello world"
        ]),
        body=OrgString([
            "Where is everybody? ",
            OrgLink(title='Fermi Paradox', url='https://en.wikipedia.org/wiki/Fermi_paradox'),
        ]),
        tags=['blue', 'red'],
        )
    assert(str(heading) == "* [2021-10-02 Sat 18:32] hello world :blue:red:\n"
                           "Where is everybody? [[https://en.wikipedia.org/wiki/Fermi_paradox][Fermi Paradox]]")

def test_file(org_file):

    # test two top level headings
    heading1 = OrgHeading(heading="hello world", body="Where is everybody?")
    heading2 = OrgHeading(heading="hello universe", body="Still nobody?")
    org_file.append_heading(heading1)
    org_file.append_heading(heading2)
    assert(str(org_file) == "* hello world\n"
                            "Where is everybody?\n"
                            "* hello universe\n"
                            "Still nobody?")

    # add subheading
    heading3 = OrgHeading(heading="Earth C-137", body="Currently Cronenberg'd")
    heading1.append_subheading(heading3)
    assert(str(org_file) == "* hello world\n"
                            "Where is everybody?\n"
                            "** Earth C-137\n"
                            "Currently Cronenberg'd\n"
                            "* hello universe\n"
                            "Still nobody?")