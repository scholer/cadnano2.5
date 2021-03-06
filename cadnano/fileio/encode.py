import io
import json
from typing import Union

import numpy as np

import cadnano.fileio.v2encode as v2encode
import cadnano.fileio.v3encode as v3encode
from cadnano.cntypes import (
    DocT
)

def encodeToFile(filename: str, document: DocT, legacy: bool = False):
    """
    Encodes the document as json object and outputs to file.

    Args:
        filename: Filename path for writing
        document: Document to encode
        legacy: Export for use with legacy (pre v2.5) cadnano versions.
    """
    json_string = encode(document, legacy)
    with io.open(filename, 'w', encoding='utf-8') as fd:
        fd.write(json_string)
# end def


def encode(document: DocT, legacy: bool = False) -> str:
    """Encodes the document as json object.

    Args:
        document: Document to encode
        legacy: Export for use with legacy (pre v2.5) cadnano versions.

    Returns:
        the json string containing the encoded document
    """
    if legacy:
        obj = v2encode.encodeDocument(document)
    else:
        obj = v3encode.encodeDocument(document)
    json_string = json.dumps(obj, separators=(',', ':'), cls=EncoderforPandas)  # compact encoding
    return json_string


class EncoderforPandas(json.JSONEncoder):
    """Special encoder to coerce numpy number types into python types.
    Or just default to a normal encoding for normal python types
    """

    def default(self, obj) -> Union[int, float, str, bool, list]:
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            try:
                return super(EncoderforPandas, self).default(obj)
            except Exception:
                print(type(obj))
                raise
# end class
