# -*- coding: utf-8 -*-

"""
Created on 2020-07-19 00:20
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com

配置模型、路径、与训练相关参数
"""

class Config(object):
    def __init__(self):
        self.config_dict = {
            "data_path": {
                "vocab_path": "../data/cnews.vocab.txt",
                "trainingSet_path": "../data/cnews.train.txt",
                "valSet_path": "../data/cnews.val.txt",
                "testingSet_path": "../data/cnews.test.txt"
            },
            "CNN_training_rule": {
                "embedding_dim": 64,
                "seq_length": 600,
                "num_classes": 10,

                "conv1_num_filters": 128,
                "conv1_kernel_size": 2,

                "conv2_num_filters": 64,
                "conv2_kernel_size": 3,

                "vocab_size": 5000,

                "hidden_dim": 128,

                "dropout_keep_prob": 0.5,
                "learning_rate": 1e-3,

                "batch_size": 64,
                "epochs": 5,

                "print_per_batch": 100,
                "save_per_batch": 1000
            },
            "result":{
                "CNN_model_path": "../result/CNN_model.h5"
            }
        }

    def get(self, section, name):
        return self.config_dict[section][name]