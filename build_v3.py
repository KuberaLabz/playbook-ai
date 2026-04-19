#!/usr/bin/env python3
"""PLAYBOOK AI v3 — Merge all extension batches into one EXT dict"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

# Import all 4 extension batches
from extensions.ext_01_07 import EXT as EXT_01_07
from extensions.ext_08_14 import EXT as EXT_08_14
from extensions.ext_15_21 import EXT as EXT_15_21
from extensions.ext_22_28 import EXT as EXT_22_28

ALL_EXT = {}
for d in [EXT_01_07, EXT_08_14, EXT_15_21, EXT_22_28]:
    ALL_EXT.update(d)

print(f"Total extensions loaded: {len(ALL_EXT)}")
print(f"Tools covered: {sorted(ALL_EXT.keys())}")

# Verify all 28 tools have extensions
from assemble_v2 import ALL_TOOLS
missing = [t[0] for t in ALL_TOOLS if t[0] not in ALL_EXT]
if missing:
    print(f"WARNING: Missing extensions for: {missing}")
else:
    print("✓ All 28 tools have extensions")
