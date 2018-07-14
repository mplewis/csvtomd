from .context import wrap

import sure  # noqa


def test_wrap():
    wrap(" ", 2, "foobar").should.equal("  foobar  ")
    wrap("!", 1, "danger will robinson").should.equal("!danger will robinson!")
    wrap("?", 0, "coffee").should.equal("coffee")
