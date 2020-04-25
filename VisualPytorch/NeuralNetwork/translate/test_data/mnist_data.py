base_start={
  "type": "base",
  "name": "base_start",
  "attribute": {
    "layer_type": "start",
  }
}
base_end={
  "type": "base",
  "name": "base_end",
  "attribute": {
    "layer_type": "end",
  }
}
base_conv1={
  "type": "base",
  "name": "base_conv1",
     "attribute": {
      "layer_type": "conv_layer",
      "attribute": {
	  "layer_type":"conv",
	  "attribute": {
        "type": "2d",
        "in_channels":"1",
		"out_channels":"10",
		"kernel_size":"5",
		"stride":"1",
		"padding":"0"
      }
    }
}
}
base_pool={
  'type':'base',
  "name":"base_pool",
  "attribute": {
    "layer_type": "pool_layer",
    "attribute": {
      "layer_type": "max_pool",
      "attribute": {
	    "type":"2d",
        "kernel_size": '2',
        "stride": '2',
        "padding": '0'
      }
    }
  }
}
base_relu={
  "type": "base",
  "name": "base_relu",
     "attribute": {
      "layer_type": "activation_layer",
      "attribute": {
        "layer_type":"relu",
    }
}
}
base_conv2={
  "type": "base",
  "name": "base_conv2",
     "attribute": {
      "layer_type": "conv_layer",
      "attribute": {
	  "layer_type":"conv",
	  "attribute": {
        "type": "2d",
        "in_channels":"10",
		"out_channels":"20",
		"kernel_size":"5",
		"stride":"1",
		"padding":"0"
      }
    }
}
}     
base_conv3={
  "type": "base",
  "name": "base_conv3",
     "attribute": {
      "layer_type": "conv_layer",
      "attribute": {
	  "layer_type":"conv",
	  "attribute": {
        "type": "2d",
        "in_channels":"20",
		"out_channels":"40",
		"kernel_size":"3",
		"stride":"1",
		"padding":"0"
      }
    }
}
}         
base_view= {
  "type": "base",
  "name": "base_view",
  "attribute": {
    "layer_type": "view_layer",

    "attribute": {
		"shape":"64,-1"
    }
  }
}
base_linear={
  "type": "base",
  "name": "base_linear",
  "attribute": {
    "layer_type": "linear_layer",

    "attribute": {
		"in_features":"40",
		"out_features":"10"
    }
  }

}
base_softmax={
  "type": "base",
  "name": "base_softmax",
  "attribute": {
    "layer_type": "softmax_layer",

    "attribute": {
		"dim":"1"
    }
  }

}
mnist_sequential={
  "type": "sequential",
  "name": "mnist_sequential",
  "attribute": {
    "in": "canvas_0",
    "out": "canvas_13",
    "nets": {
      "canvas_0":base_start,
      "canvas_1": base_conv1,
      "canvas_2": base_pool,
	  "canvas_3":base_relu,
	  "canvas_4":base_conv2,
      "canvas_5":base_pool,
      "canvas_6":base_relu,
      "canvas_7":base_conv3,
      "canvas_8":base_pool,
	  "canvas_9":base_relu,
      "canvas_10":base_view,
      "canvas_11":base_linear,
      "canvas_12":base_softmax,
      "canvas_13":base_end
    }
	},
    "nets_conn": [
               {
             "source": {
                "id": "canvas_0"
             },
             "target": {
                 "id": "canvas_1"
             }
         },
		                {
             "source": {
                "id": "canvas_1"
             },
             "target": {
                 "id": "canvas_2"
             }
         },
		                {
             "source": {
                "id": "canvas_2"
             },
             "target": {
                 "id": "canvas_3"
             }
         },
		                {
             "source": {
                "id": "canvas_3"
             },
             "target": {
                 "id": "canvas_4"
             }
         }   ,
              {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_5"
             }
         } ,   {
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_6"
             }
         } ,{
             "source": {
                "id": "canvas_6"
             },
             "target": {
                 "id": "canvas_7"
             }
         },{
             "source": {
                "id": "canvas_7"
             },
             "target": {
                 "id": "canvas_8"
             }
         },{
             "source": {
                "id": "canvas_8"
             },
             "target": {
                 "id": "canvas_9"
             }
         },{
             "source": {
                "id": "canvas_9"
             },
             "target": {
                 "id": "canvas_10"
             }
         },{
             "source": {
                "id": "canvas_10"
             },
             "target": {
                 "id": "canvas_11"
             }
         },{
             "source": {
                "id": "canvas_11"
             },
             "target": {
                 "id": "canvas_12"
             }
         },{
             "source": {
                "id": "canvas_12"
             },
             "target": {
                 "id": "canvas_13"
             }
         }
    ]
}   
test_data={
  "epoch": '1',
  "learning_rate": '0.01',
  "batch_size": '64',
  "dataset": "mnist",
  "if_shuffle": 'true',
  "platform": "cpu",

  "learning_rate_scheduler": 'None',
  "optimizer": {
    "name": "SGD",
    "attribute": {
      "momentum":'0.5',
      "weight_decay":'0',
      "dampening":'0',
      'nesterov':'False'
    }
  },


  "loss": {
    "name": "NLLLoss",
    "attribute": {
      "weight":"None",
      "ignore_index": "None",
      "reduction":"mean"
    }
  }
}
data={
  "canvas": mnist_sequential,
  "static": test_data
}