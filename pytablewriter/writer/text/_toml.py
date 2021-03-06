# encoding: utf-8

from __future__ import absolute_import, unicode_literals

from ._text_writer import TextTableWriter


class TomlTableWriter(TextTableWriter):
    """
    A table writer class for
    `TOML <https://github.com/toml-lang/toml>`__ data format.

        :Example:
            :ref:`example-toml-table-writer`
    """

    FORMAT_NAME = "toml"

    @property
    def format_name(self):
        return self.FORMAT_NAME

    @property
    def support_split_write(self):
        return True

    def __init__(self):
        super(TomlTableWriter, self).__init__()

        self.is_formatting_float = False

        self._is_require_table_name = True
        self._is_require_header = True

    def write_table(self):
        """
        |write_table| with
        `TOML <https://github.com/toml-lang/toml>`__ format.

        :raises pytablewriter.EmptyTableNameError:
            If the |headers| is empty.
        :raises pytablewriter.EmptyHeaderError:
            If the |headers| is empty.
        :Example:
            :ref:`example-toml-table-writer`
        """

        import toml

        with self._logger:
            self._verify_property()
            self.stream.write(toml.dumps(self.tabledata.as_dict()))
