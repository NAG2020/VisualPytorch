data={
    "canvas": [
        {
            "type": "sequential",
            "name": "sequential_",
            "attribute": {
                "in": "canvas_1",
                "out": "canvas_16",
                "nets": {
                    "canvas_1": {
                        "type": "base",
                        "name": "start",
                        "attribute": {
                            "start": "true"
                        },
                        "left": "119px",
                        "top": "72px"
                    },
                    "canvas_4": {
                        "type": "base",
                        "name": "conv_layer",
                        "attribute": {
                            "layer_type": "conv",
                            "type": "2d",
                            "in_channels": "1",
                            "out_channels": "10",
                            "kernel_size": "5",
                            "stride": "1",
                            "padding": "0"
                        },
                        "left": "125px",
                        "top": "138px"
                    },
                    "canvas_5": {
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
                        "left": "29px",
                        "top": "221px"
                    },
                    "canvas_6": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "164px",
                        "top": "306px"
                    },
                    "canvas_7": {
                        "type": "base",
                        "name": "conv_layer",
                        "attribute": {
                            "layer_type": "conv",
                            "type": "2d",
                            "in_channels": "10",
                            "out_channels": "20",
                            "kernel_size": "5",
                            "stride": "1",
                            "padding": "0"
                        },
                        "left": "72px",
                        "top": "400px"
                    },
                    "canvas_8": {
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
                        "left": "151px",
                        "top": "483px"
                    },
                    "canvas_9": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "62px",
                        "top": "571px"
                    },
                    "canvas_10": {
                        "type": "base",
                        "name": "conv_layer",
                        "attribute": {
                            "layer_type": "conv",
                            "type": "2d",
                            "in_channels": "20",
                            "out_channels": "40",
                            "kernel_size": "3",
                            "stride": "1",
                            "padding": "0"
                        },
                        "left": "251px",
                        "top": "617px"
                    },
                    "canvas_11": {
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
                        "left": "76px",
                        "top": "718px"
                    },
                    "canvas_12": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "67px",
                        "top": "790px"
                    },
                    "canvas_13": {
                        "type": "base",
                        "name": "view_layer",
                        "attribute": {
                            "shape": "32,40"
                        },
                        "left": "262px",
                        "top": "823px"
                    },
                    "canvas_14": {
                        "type": "base",
                        "name": "linear_layer",
                        "attribute": {
                            "in_features": "40",
                            "out_features": "10"
                        },
                        "left": "269px",
                        "top": "885px"
                    },
                    "canvas_15": {
                        "type": "base",
                        "name": "softmax_layer",
                        "attribute": {
                            "dim": "1"
                        },
                        "left": "132px",
                        "top": "885px"
                    },
                    "canvas_16": {
                        "type": "base",
                        "name": "end",
                        "attribute": {
                            "end": "true"
                        },
                        "left": "14px",
                        "top": "951px"
                    }
                }
            },
            "nets_conn": [
                {
                    "source": {
                        "id": "canvas_12",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_13",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_13",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_14",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_14",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_15",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_15",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_16",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_1",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_4",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_4",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_5",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_5",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_6",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_6",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_7",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_7",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_8",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_8",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_9",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_9",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_10",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_10",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_11",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_11",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_12",
                        "anchor_position": "Top"
                    }
                }
            ]
        }
    ],
    "static": {
        "epoch": "1",
        "learning_rate": "0.01",
        "batch_size": "64",
        "learning_rate_scheduler": {
            "name": "None",
            "attribute": {
                "step_size": 50,
                "gramma": 0.1
            }
        },
        "device": "cpu",
        "data": "mnist",
        "optimizer": {
            "name": "SGD",
            "attribute": {
                "momentum": "0.5"
            }
        },
        "loss": {
            "name": "NLLLoss",
            "attribute": {
                "reduction": "mean"
            }
        }
    }