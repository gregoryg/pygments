"""
    pygments.lexers.gsql
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for TigerGraph GSQL graph query language

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, using, this, words
from pygments.token import Keyword, Punctuation, Comment, Operator, Name,\
    String, Number, Whitespace, Token


__all__ = ["GSQLLexer"]

class GSQLLexer(RegexLexer):

    """
    For `GSQL <https://docs.tigergraph.com/dev/gsql-ref>`_ queries (version 3.x).
    .. versionadded:: 2.10
    """

    name = 'GSQL'
    aliases = ['gsql']
    filenames = ['*.gsql']

    flags = re.MULTILINE | re.IGNORECASE

    tokens = {
        'root': [
            include('comment'),
            include('keywords'),
            include('clauses'),
            include('accums'),
            include('relations'),
            include('functions'),
            include('strings'),
            include('whitespace'),
            include('barewords'),
            include('operators'),
        ],
        'comment': [
            (r'\#.*', Comment.Single),
            (r'/\*(.|\n)*?\*/', Comment.Multiline),
        ],
        'keywords': [
            (words((
             'ACCUM', 'AND', 'ANY', 'API', 'AS', 'ASC', 'BAG', 'BATCH', 'BETWEEN', 'BOOL', 'BOTH',
             'BREAK', 'BY', 'CASE', 'CATCH', 'COMPRESS', 'CONTINUE', 'COUNT',
             'CREATE', 'DATETIME', 'DELETE', 'DESC', 'DISTRIBUTED', 'DO',
             'DOUBLE', 'EDGE', 'ELSE', 'END', 'ESCAPE', 'EXCEPTION', 'FALSE', 'FILE', 'FLOAT', 'FOREACH', 'FOR',
             'FROM', 'GRAPH', 'GROUP', 'GSQL_INT_MAX', 'GSQL_INT_MIN', 'GSQL_UINT_MAX', 'HAVING', 'IF',
             'IN', 'INSERT', 'INT', 'INTERPRET', 'INTERSECT', 'INTERVAL', 'INTO', 'IS', 'ISEMPTY', 'JSONARRAY', 'JSONOBJECT', 'LASTHOP',
             'LEADING', 'LIKE', 'LIMIT', 'LIST', 'LOAD_ACCUM', 'MAP', 'MATCH', 'MINUS', 'NOT',
             'NULL', 'OFFSET', 'OR', 'ORDER', 'PATH', 'PER', 'PINNED', 'POST_ACCUM', 'POST-ACCUM', 'PRIMARY_ID', 'PRINT',

             'QUERY', 'RAISE', 'RANGE', 'REPLACE', 'RESET_COLLECTION_ACCUM', 'RETURN', 'RETURNS', 'RUN', 'SAMPLE', 'SELECT', 'SELECT_VERTEX',
             'SET', 'SRC', 'STATIC', 'STRING', 'SYNTAX', 'TARGET', 'TAGSTGT', 'THEN', 'TO', 'TO_CSV', 'TRAILING', 'TRUE',
             'TRY', 'TUPLE', 'TYPEDEF', 'UINT', 'UNION', 'UPDATE', 'VALUES', 'VERTEX', 'WHEN', 'WHERE', 'WHILE', 'WITH'), prefix=r'(?<!\.)', suffix=r'\b'), Token.Keyword)
        ],
        'clauses': [
            (words(('accum', 'having', 'limit', 'order', 'postAccum', 'sample', 'where')), Name.Builtin)
        ],
        'accums': [
            (words(('andaccum', 'arrayaccum', 'avgaccum', 'bagaccum', 'bitwiseandaccum',
             'bitwiseoraccum', 'groupbyaccum', 'heapaccum', 'listaccum', 'MapAccum',
             'maxaccum', 'minaccum', 'oraccum', 'setaccum', 'sumaccum')), Name.Builtin),
        ],
        'functions':[
            (words(('abs', 'acos', 'addTags', 'ascii', 'asin', 'atan', 'atan2', 'avg', 'ceil',
                   'chr', 'clear', 'coalesce', 'concat', 'contains', 'containsKey', 'cos', 'cosh', 'count',
                    'datetime_add', 'datetime_diff', 'datetime_format', 'datetime_sub',
                   'datetime_to_epoch', 'day', 'degrees', 'difference', 'differenceTags',
                   'edgeAttribute', 'epoch_to_datetime', 'evaluate', 'exp', 'filter', 'find_in_set',
                   'flatten', 'flatten_json_array', 'float_to_int', 'floor', 'fmod', 'get', 'getAttr',
                   'getBool', 'getDouble', 'getInt', 'getJsonArray', 'getJsonObject', 'getString',
                   'getTags', 'getvid', 'gsql_concat', 'gsql_current_time_epoch', 'gsql_day',
                   'gsql_day_epoch', 'gsql_find', 'gsql_is_false', 'gsql_is_not_empty_string',
                   'gsql_is_true', 'gsql_length', 'gsql_lower', 'gsql_ltrim', 'gsql_month',
                   'gsql_month_epoch', 'gsql_regex_match', 'gsql_regex_replace',
                   'gsql_replace', 'gsql_reverse', 'gsql_rtrim', 'gsql_split_by_space',
                   'gsql_substring', 'gsql_to_bool', 'gsql_to_int', 'gsql_to_uint',
                   'gsql_token_equal', 'gsql_token_ignore_case_equal', 'gsql_trim',
                   'gsql_ts_to_epoch_seconds', 'gsql_upper', 'gsql_uuid_v4', 'gsql_year',
                   'gsql_year_epoch', 'hasTags', 'hour', 'ignore_if_exists', 'instr',
                   'intersectTags', 'isDirected', 'isTaggable', 'ldexp', 'left', 'length', 'log', 'log10',
                   'log2', 'lower', 'lpad', 'ltrim', 'max', 'min', 'minute', 'month', 'neighborAttribute',
                   'neighbors', 'now', 'outdegree', 'overwrite', 'parse_json_array',
                   'parse_json_object', 'PI', 'pop', 'pow', 'println', 'radians', 'rand', 'reallocate',
                   'reduce', 'remove', 'removeAll', 'removeAllTags', 'removeTags', 'replace', 'resize',
                   'right', 'round', 'rpad', 'rtrim', 'second', 'selectVertex', 'setAttr', 'sign', 'sin',
                   'sinh', 'size', 'soundex', 'space', 'split', 'sqrt', 'square', 'str_to_int', 'substr',
                   'sum', 'tan', 'tanh', 'to_datetime', 'to_float', 'to_int', 'to_string', 'to_vertex',
                   'to_vertex_set', 'token_len', 'top', 'translate', 'trim', 'trunc', 'type', 
                    'upper', 'year')), Name.Function),
        ],
        'relations': [
            (r'(-\s?)(\(.*\:\w?\))(\s?-)', bygroups(Operator, using(this), Operator)),
            (r'->|<-', Operator),
            (r'[.*{}\[\]\<\>\_]', Punctuation),
        ],
        'strings': [
            (r'"([^"\\]|\\.)*"', String),
            (r'@{1,2}\w+', Name.Variable),
        ],
        'whitespace': [
            (r'\s+', Whitespace),
        ],
        'barewords': [
            (r'[a-z]\w*', Name),
            (r'(\d+\.\d+|\d+)', Number),
        ],
        'operators': [
            (r'\$|[^0-9|\/|\-](\-\=|\+\=|\*\=|\\\=|\=|\=\=|\=\=\=|\+|\-|\*|\\|\+\=|\>|\<)[^\>|\/]', Operator),
            (r'(\||\(|\)|\,|\;|\=|\-|\+|\*|\/|\>|\<|\:)', Operator),
        ],
    }
