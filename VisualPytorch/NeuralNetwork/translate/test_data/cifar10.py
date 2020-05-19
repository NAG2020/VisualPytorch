data={
    "canvas": [
        {
            "type": "sequential",
            "name": "sequential_",
            "attribute": {
                "in": "canvas_17",
                "out": "canvas_30",
                "nets": {
                    "canvas_17": {
                        "type": "base",
                        "name": "start",
                        "attribute": {
                            "start": "true"
                        },
                        "left": "122px",
                        "top": "77px"
                    },
                    "canvas_18": {
                        "type": "base",
                        "name": "conv_layer",
                        "attribute": {
                            "layer_type": "conv",
                            "type": "2d",
                            "in_channels": "3",
                            "out_channels": "6",
                            "kernel_size": "5",
                            "stride": "1",
                            "padding": "0"
                        },
                        "left": "73px",
                        "top": "198px"
                    },
                    "canvas_19": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "73px",
                        "top": "297px"
                    },
                    "canvas_20": {
                        "type": "base",
                        "name": "pool_layer",
                        "attribute": {
                            "layer_type": "max_pool",
                            "type": "2d",
                            "kernel_size": "2",
                            "stride": "2",
                            "padding": "0",
                            "ceil_mode": "floor",
                            "count_include_pad": "True"
                        },
                        "left": "83px",
                        "top": "400px"
                    },
                    "canvas_21": {
                        "type": "base",
                        "name": "conv_layer",
                        "attribute": {
                            "layer_type": "conv",
                            "type": "2d",
                            "in_channels": "6",
                            "out_channels": "16",
                            "kernel_size": "5",
                            "stride": "1",
                            "padding": "0"
                        },
                        "left": "79px",
                        "top": "495px"
                    },
                    "canvas_22": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "89px",
                        "top": "572px"
                    },
                    "canvas_23": {
                        "type": "base",
                        "name": "pool_layer",
                        "attribute": {
                            "layer_type": "max_pool",
                            "type": "2d",
                            "kernel_size": "2",
                            "stride": "2",
                            "padding": "0",
                            "ceil_mode": "floor",
                            "count_include_pad": "True"
                        },
                        "left": "72px",
                        "top": "654px"
                    },
                    "canvas_24": {
                        "type": "base",
                        "name": "view_layer",
                        "attribute": {
                            "shape": "100,400"
                        },
                        "left": "66px",
                        "top": "717px"
                    },
                    "canvas_25": {
                        "type": "base",
                        "name": "linear_layer",
                        "attribute": {
                            "in_features": "400",
                            "out_features": "120"
                        },
                        "left": "63px",
                        "top": "785px"
                    },
                    "canvas_26": {
                        "type": "base",
                        "name": "linear_layer",
                        "attribute": {
                            "in_features": "120",
                            "out_features": "84"
                        },
                        "left": "65px",
                        "top": "924px"
                    },
                    "canvas_27": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "65px",
                        "top": "853px"
                    },
                    "canvas_28": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "280px",
                        "top": "464px"
                    },
                    "canvas_29": {
                        "type": "base",
                        "name": "linear_layer",
                        "attribute": {
                            "in_features": "84",
                            "out_features": "10"
                        },
                        "left": "294px",
                        "top": "575px"
                    },
                    "canvas_30": {
                        "type": "base",
                        "name": "end",
                        "attribute": {
                            "end": "true"
                        },
                        "left": "255px",
                        "top": "696px"
                    }
                }
            },
            "nets_conn": [
                {
                    "source": {
                        "id": "canvas_17",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_18",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_18",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_19",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_19",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_20",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_20",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_21",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_21",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_22",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_22",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_23",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_23",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_24",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_24",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_25",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_25",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_27",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_27",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_26",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_26",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_28",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_28",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_29",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_29",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_30",
                        "anchor_position": "Top"
                    }
                }
            ]
        }
    ],
    "static": {
        "epoch": "1",
        "learning_rate": "0.001",
        "batch_size": "100",
        "learning_rate_scheduler": {
            "name": "None",
            "attribute": {
                "step_size": 50,
                "gramma": 0.1
            }
        },
        "device": "cpu",
        "data": "cifar10",
        "optimizer": {
            "name": "Adam",
            "attribute": {
                "momentum": "0.5"
            }
        },
        "loss": {
            "name": "CrossEntropyLoss",
            "attribute": {
                "reduction": "mean"
            }
        }
    }
}