from .context import wrap, col_widths

import sure  # noqa


def test_wrap():
    wrap("!", 1, "danger will robinson").should.equal("!danger will robinson!")
    wrap(" ", 2, "iced mocha").should.equal("  iced mocha  ")
    wrap("?", 0, "coffee").should.equal("coffee")


def test_col_widths():
    table = [["a", "b", "c"], ["1", "22", "333"]]
    col_widths(table).should.equal([1, 2, 3])
