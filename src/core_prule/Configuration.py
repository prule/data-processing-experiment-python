from typing import List
from dataclasses import dataclass


@dataclass
class ColumnDefinition(object):
    """description goes here"""
    names: List[str]
    alias: str
    description: str
    type: str
    formats: List[str]
    required: bool
    trim: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get('names'),
            data.get('alias'),
            data.get('description'),
            data.get('type'),
            data.get('formats'),
            data.get('required'),
            data.get('trim')
        )

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.names, self.alias, self.description, self.type, self.formats, self.required, self.trim)



@dataclass
class TableDefinition(object):
    name: str
    description: str
    deduplicate: bool
    delimiter: str
    columns: List[ColumnDefinition]
    trim: bool

    def delimiter_or_default(self):
        if not self.delimiter:
            return ","
        return self.delimiter

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get('name'),
            data.get('description'),
            data.get('deduplicate'),
            data.get('delimiter'),
            list(map(ColumnDefinition.from_dict, data.get('columns'))),
            data.get('trim')
        )

    def __str__(self):
        return "{0} {1} {2} {3}".format( self.name, self.description, self.deduplicate, self.delimiter, self.trim, self.columns)


@dataclass
class SourceDefinition(object):
    key: str
    name: str
    description: str
    path: str
    type: str
    table: TableDefinition

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.key, self.name, self.description, self.path, self.type, self.table)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get('id'),
            data.get('name'),
            data.get('description'),
            data.get('path'),
            data.get('type'),
            TableDefinition.from_dict(data.get('table'))
        )


@dataclass
class Sources(object):
    key: str
    name: str
    description: str
    sources: List[SourceDefinition]

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.key, self.name, self.description, self.sources)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get('id'),
            data.get('name'),
            data.get('description'),
            list(map(SourceDefinition.from_dict, data.get('sources')))
        )
