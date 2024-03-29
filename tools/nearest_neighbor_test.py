# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import sys
from argparse import Namespace
from typing import Any, List

from vissl.config import AttrDict
from vissl.utils.hydra_config import compose_hydra_configuration, convert_to_attrdict
from vissl.utils.knn_utils import (
    extract_features_and_run_knn,
    extract_features_and_run_knn_on_slurm,
)
from vissl.utils.slurm import is_submitit_available


def main(args: Namespace, config: AttrDict):
    if config.SLURM.USE_SLURM:
        assert (
            is_submitit_available()
        ), "Please 'pip install submitit' to schedule jobs on SLURM"
        extract_features_and_run_knn_on_slurm(config)
    else:
        extract_features_and_run_knn(args.node_id, config)


def hydra_main(overrides: List[Any]):
    cfg = compose_hydra_configuration(overrides)
    args, config = convert_to_attrdict(cfg)
    main(args, config)


def invoke_main() -> None:
    overrides = sys.argv[1:]
    hydra_main(overrides=overrides)


if __name__ == "__main__":
    invoke_main()  # pragma: no cover
