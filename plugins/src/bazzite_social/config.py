# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from mkdocs.config.base import Config
from mkdocs.config.config_options import Type, Optional

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------

# Social plugin configuration
class SocialConfig(Config):
    enabled = Type(bool, default = True)
    cache_dir = Type(str, default = ".cache/plugin/bazzite-social")
    
    # Settings for social cards
    cards = Type(bool, default = True)
    cards_dir = Type(str, default = "assets/images/bazzite-social")
    cards_layout_options = Type(dict, default = {})

    # Deprecated settings
    cards_color = Type(dict, default = {})
    cards_font = Optional(Type(str))
