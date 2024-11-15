# Auto generated from hello.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-15T16:05:32
# Schema: hello
#
# id: https://hello-linkml.mkbrechtel.dev/model/
# description: A schema for storing hello world messages in different languages
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
HELLO = CurieNamespace('hello', 'https://hello-linkml.mkbrechtel.dev/model/')
ISO639 = CurieNamespace('iso639', 'http://id.loc.gov/vocabulary/iso639-1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HELLO


# Types

# Class references
class MessageId(extended_str):
    pass


@dataclass(repr=False)
class Message(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HELLO["Message"]
    class_class_curie: ClassVar[str] = "hello:Message"
    class_name: ClassVar[str] = "Message"
    class_model_uri: ClassVar[URIRef] = HELLO.Message

    id: Union[str, MessageId] = None
    text: str = None
    language: Optional[Union[str, "LanguageCode"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MessageId):
            self.id = MessageId(self.id)

        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.language is not None and not isinstance(self.language, LanguageCode):
            self.language = LanguageCode(self.language)

        super().__post_init__(**kwargs)


# Enumerations
class LanguageCode(EnumDefinitionImpl):
    """
    ISO 639-1 language codes
    """
    ar = PermissibleValue(
        text="ar",
        description="Arabic",
        meaning=ISO639["ar"])
    bn = PermissibleValue(
        text="bn",
        description="Bengali",
        meaning=ISO639["bn"])
    zh = PermissibleValue(
        text="zh",
        description="Chinese",
        meaning=ISO639["zh"])
    cs = PermissibleValue(
        text="cs",
        description="Czech",
        meaning=ISO639["cs"])
    da = PermissibleValue(
        text="da",
        description="Danish",
        meaning=ISO639["da"])
    nl = PermissibleValue(
        text="nl",
        description="Dutch",
        meaning=ISO639["nl"])
    en = PermissibleValue(
        text="en",
        description="English",
        meaning=ISO639["en"])
    fi = PermissibleValue(
        text="fi",
        description="Finnish",
        meaning=ISO639["fi"])
    fr = PermissibleValue(
        text="fr",
        description="French",
        meaning=ISO639["fr"])
    de = PermissibleValue(
        text="de",
        description="German",
        meaning=ISO639["de"])
    el = PermissibleValue(
        text="el",
        description="Greek",
        meaning=ISO639["el"])
    hi = PermissibleValue(
        text="hi",
        description="Hindi",
        meaning=ISO639["hi"])
    hu = PermissibleValue(
        text="hu",
        description="Hungarian",
        meaning=ISO639["hu"])
    id = PermissibleValue(
        text="id",
        description="Indonesian",
        meaning=ISO639["id"])
    ga = PermissibleValue(
        text="ga",
        description="Irish",
        meaning=ISO639["ga"])
    it = PermissibleValue(
        text="it",
        description="Italian",
        meaning=ISO639["it"])
    ja = PermissibleValue(
        text="ja",
        description="Japanese",
        meaning=ISO639["ja"])
    ko = PermissibleValue(
        text="ko",
        description="Korean",
        meaning=ISO639["ko"])
    fa = PermissibleValue(
        text="fa",
        description="Persian",
        meaning=ISO639["fa"])
    pl = PermissibleValue(
        text="pl",
        description="Polish",
        meaning=ISO639["pl"])
    pt = PermissibleValue(
        text="pt",
        description="Portuguese",
        meaning=ISO639["pt"])
    ru = PermissibleValue(
        text="ru",
        description="Russian",
        meaning=ISO639["ru"])
    es = PermissibleValue(
        text="es",
        description="Spanish",
        meaning=ISO639["es"])
    sv = PermissibleValue(
        text="sv",
        description="Swedish",
        meaning=ISO639["sv"])
    th = PermissibleValue(
        text="th",
        description="Thai",
        meaning=ISO639["th"])
    tr = PermissibleValue(
        text="tr",
        description="Turkish",
        meaning=ISO639["tr"])
    uk = PermissibleValue(
        text="uk",
        description="Ukrainian",
        meaning=ISO639["uk"])
    vi = PermissibleValue(
        text="vi",
        description="Vietnamese",
        meaning=ISO639["vi"])

    _defn = EnumDefinition(
        name="LanguageCode",
        description="ISO 639-1 language codes",
    )

# Slots
class slots:
    pass

slots.message__id = Slot(uri=HELLO.id, name="message__id", curie=HELLO.curie('id'),
                   model_uri=HELLO.message__id, domain=None, range=URIRef)

slots.message__text = Slot(uri=HELLO.text, name="message__text", curie=HELLO.curie('text'),
                   model_uri=HELLO.message__text, domain=None, range=str)

slots.message__language = Slot(uri=HELLO.language, name="message__language", curie=HELLO.curie('language'),
                   model_uri=HELLO.message__language, domain=None, range=Optional[Union[str, "LanguageCode"]])
