"""
SPDX-FileCopyrightText: 2025 DESY and the Constellation authors
SPDX-License-Identifier: EUPL-1.2
"""

import time

from constellation.core.configuration import Configuration
from constellation.core.satellite import Satellite


class TempMon(Satellite):
    _time_to_throw: float | int

    def do_initializing(self, config: Configuration) -> str:
        self._time_to_throw = config.setdefault("time_to_throw", 10)
        return "Initialized"

    def do_run(self, run_identifier: str) -> str:
        time.sleep(float(self._time_to_throw))
        msg = "Temperature above critical threshold!"
        self.log.critical(msg)
        raise Exception(msg)
        return ""
