# Copyright 2023 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Top-level presubmit script for infra.

See http://dev.chromium.org/developers/how-tos/depottools/presubmit-scripts for
details on the presubmit API built into gcl.
"""

import os

PRESUBMIT_VERSION = '2.0.0'
USE_PYTHON3 = True

def CheckCommon(input_api, output_api):  # pragma: no cover
  return input_api.canned_checks.PanProjectChecks(input_api, output_api,
                                                  owners_check=False)
