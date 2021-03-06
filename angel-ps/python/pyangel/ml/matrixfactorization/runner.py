#
# Tencent is pleased to support the open source community by making Angel available.
#
# Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
# https://opensource.org/licenses/Apache-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
#

import tempfile

from hadoop.local_fs import LocalFileSystem

from pyangel.conf import AngelConf
from pyangel.conf import Configuration
from pyangel.ml.conf import MLConf
from pyangel.ml.client.angel_client_factory import AngelClientFactory
from pyangel.ml_runner import MLRunner

class MatrixFactorizationRunner(MLRunner):

    def train(self, conf):
        """
        Training job to obtain a model
        :param conf: configuration for parameter settings
        """
        jconf = conf.dict_to_jconf()
        super(MatrixFactorizationRunner, self).train(conf, conf._jvm.com.tencent.angel.ml.matrixfactorization.MFModel(jconf, None), 'com.tencent.angel.ml.matrixfactorization.MFTrainTask')
