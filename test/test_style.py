# encoding: utf-8

from __future__ import print_function, unicode_literals

import sys

import pytest
from pytablewriter.style import Align, FontSize, FontStyle, FontWeight, Style, ThousandSeparator


class Test_Style_constructor(object):
    @pytest.mark.parametrize(
        ["value", "expected"],
        [
            [
                {
                    "align": Align.RIGHT,
                    "font_size": FontSize.TINY,
                    "font_weight": FontWeight.BOLD,
                    "thousand_separator": ThousandSeparator.SPACE,
                },
                {
                    "align": Align.RIGHT,
                    "font_size": FontSize.TINY,
                    "font_weight": FontWeight.BOLD,
                    "thousand_separator": ThousandSeparator.SPACE,
                },
            ],
            [
                {
                    "align": "left",
                    "font_size": "small",
                    "font_weight": "bold",
                    "thousand_separator": ",",
                },
                {
                    "align": Align.LEFT,
                    "font_size": FontSize.SMALL,
                    "font_weight": FontWeight.BOLD,
                    "thousand_separator": ThousandSeparator.COMMA,
                },
            ],
            [
                {"font_size": "TINY"},
                {
                    "align": Align.AUTO,
                    "font_size": FontSize.TINY,
                    "font_weight": FontWeight.NORMAL,
                    "thousand_separator": ThousandSeparator.NONE,
                },
            ],
        ],
    )
    def test_normal(self, value, expected):
        style = Style(**value)

        print("expected: {}\nactual: {}".format(expected, style), file=sys.stderr)

        assert style.align is expected.get("align")
        assert style.font_size is expected.get("font_size")
        assert style.font_weight is expected.get("font_weight")
        assert style.thousand_separator is expected.get("thousand_separator")


class Test_Style_eq(object):
    @pytest.mark.parametrize(
        ["lhs", "rhs", "expected"],
        [
            [Style(), Style(), True],
            [Style(align=Align.RIGHT), Style(align=Align.RIGHT), True],
            [Style(align=Align.RIGHT), Style(align=Align.LEFT), False],
            [Style(align=Align.RIGHT), Style(align="right"), True],
            [Style(align=Align.RIGHT), Style(align=Align.RIGHT, font_size=FontSize.TINY), False],
            [Style(font_size=FontSize.TINY), Style(font_size=FontSize.TINY), True],
            [Style(font_size=FontSize.TINY), Style(font_size="tiny"), True],
            [Style(font_size=FontSize.TINY), Style(font_size=FontSize.LARGE), False],
            [Style(font_weight="bold"), Style(font_weight=FontWeight.BOLD), True],
            [Style(font_weight="bold"), Style(font_weight="normal"), False],
            [Style(font_style="italic"), Style(font_style=FontStyle.ITALIC), True],
            [Style(font_style="italic"), Style(font_style="normal"), False],
            [Style(thousand_separator=","), Style(thousand_separator=","), True],
            [Style(thousand_separator=","), Style(thousand_separator="comma"), True],
            [Style(thousand_separator=""), Style(thousand_separator=","), False],
            [
                Style(thousand_separator=ThousandSeparator.COMMA),
                Style(thousand_separator=ThousandSeparator.COMMA),
                True,
            ],
            [
                Style(thousand_separator="space"),
                Style(thousand_separator=ThousandSeparator.SPACE),
                True,
            ],
            [
                Style(thousand_separator=ThousandSeparator.COMMA),
                Style(thousand_separator=ThousandSeparator.COMMA, font_size=FontSize.TINY),
                False,
            ],
            [
                Style(
                    align=Align.LEFT,
                    font_size=FontSize.TINY,
                    font_style=FontStyle.ITALIC,
                    font_weight=FontWeight.BOLD,
                    thousand_separator=ThousandSeparator.COMMA,
                ),
                Style(
                    align="left",
                    font_size="tiny",
                    font_style="italic",
                    font_weight="bold",
                    thousand_separator=",",
                ),
                True,
            ],
            [Style(), None, False],
        ],
    )
    def test_normal(self, lhs, rhs, expected):
        assert (lhs == rhs) == expected
        assert (lhs != rhs) != expected

    @pytest.mark.parametrize(
        ["align", "font_size", "thousand_separator", "expected"],
        [
            ["invali", None, None, TypeError],
            [FontSize.TINY, None, None, TypeError],
            [None, "invali", None, TypeError],
            [None, Align.LEFT, None, TypeError],
            [None, None, "invalid", TypeError],
        ],
    )
    def test_exception(self, align, font_size, thousand_separator, expected):
        with pytest.raises(expected):
            Style(align=align, font_size=font_size, thousand_separator=thousand_separator)


class Test_Style_repr(object):
    @pytest.mark.parametrize(
        ["value", "expected"],
        [
            [
                Style(
                    align="left",
                    font_size="tiny",
                    font_style="italic",
                    font_weight="bold",
                    thousand_separator=",",
                ),
                "(align=left, font_size=tiny, font_style=italic, font_weight=bold, thousand_separator=comma)",
            ],
            [Style(), "(align=auto, font_style=normal, font_weight=normal)"],
        ],
    )
    def test_normal(self, value, expected):
        assert str(value) == expected
