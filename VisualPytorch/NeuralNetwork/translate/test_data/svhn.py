data={
    "canvas": [
        {
            "type": "sequential",
            "name": "sequential_",
            "attribute": {
                "in": "canvas_31",
                "out": "canvas_44",
                "nets": {
                    "canvas_31": {
                        "type": "base",
                        "name": "start",
                        "attribute": {
                            "start": "true"
                        },
                        "left": "196px",
                        "top": "-5px"
                    },
                    "canvas_32": {
                        "type": "base",
                        "name": "conv_layer",
                        "attribute": {
                            "layer_type": "conv",
                            "type": "2d",
                            "in_channels": "3",
                            "out_channels": "10",
                            "kernel_size": "5",
                            "stride": "1",
                            "padding": "0"
                        },
                        "left": "133px",
                        "top": "85px"
                    },
                    "canvas_33": {
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
                        "left": "130px",
                        "top": "166px"
                    },
                    "canvas_34": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "128px",
                        "top": "247px"
                    },
                    "canvas_35": {
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
                        "left": "121px",
                        "top": "341px"
                    },
                    "canvas_36": {
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
                        "left": "128px",
                        "top": "445px"
                    },
                    "canvas_37": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "125px",
                        "top": "538px"
                    },
                    "canvas_38": {
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
                        "left": "143px",
                        "top": "604px"
                    },
                    "canvas_39": {
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
                        "left": "96px",
                        "top": "675px"
                    },
                    "canvas_40": {
                        "type": "base",
                        "name": "activation_layer",
                        "attribute": {
                            "layer_type": "relu",
                            "negative_slope": "0.01",
                            "weight": "0.25",
                            "lower": "0.125",
                            "upper": "0.333"
                        },
                        "left": "106px",
                        "top": "734px"
                    },
                    "canvas_41": {
                        "type": "base",
                        "name": "view_layer",
                        "attribute": {
                            "shape": "64,-1"
                        },
                        "left": "101px",
                        "top": "809px"
                    },
                    "canvas_42": {
                        "type": "base",
                        "name": "linear_layer",
                        "attribute": {
                            "in_features": "40",
                            "out_features": "10"
                        },
                        "left": "99px",
                        "top": "883px"
                    },
                    "canvas_43": {
                        "type": "base",
                        "name": "softmax_layer",
                        "attribute": {
                            "dim": "1"
                        },
                        "left": "307px",
                        "top": "358px"
                    },
                    "canvas_44": {
                        "type": "base",
                        "name": "end",
                        "attribute": {
                            "end": "true"
                        },
                        "left": "294px",
                        "top": "456px"
                    }
                }
            },
            "nets_conn": [
                {
                    "source": {
                        "id": "canvas_31",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_32",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_32",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_33",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_33",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_34",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_34",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_35",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_35",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_36",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_36",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_37",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_37",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_38",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_38",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_39",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_39",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_40",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_40",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_41",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_41",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_42",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_42",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_43",
                        "anchor_position": "Top"
                    }
                },
                {
                    "source": {
                        "id": "canvas_43",
                        "anchor_position": "Bottom"
                    },
                    "target": {
                        "id": "canvas_44",
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
        "data": "svhn",
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
}