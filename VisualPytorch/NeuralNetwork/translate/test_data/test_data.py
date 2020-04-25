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
base_pool={
  "name": "base_1",
  "attribute": {
    "layer_type": "pool_layer",
    "attribute": {
      "layer_type": "max_pool",
      "attribute": {
	    "type":"1d",
        "kernel_size": '2',
        "stride": '2',
        "padding": '0'
      }
    }
  }
}
base_concate= {
  "type": "base",
  "name": "base_2",
  "attribute": {
    "layer_type": "concatenate_layer",

    "attribute": {
		"dim":"1"
    }
  }
}
base_view= {
  "type": "base",
  "name": "base_3",
  "attribute": {
    "layer_type": "view_layer",

    "attribute": {
		"shape":"1,2,3,4"
    }
  }
}
base_element={

  "type": "base",
  "name": "base_4",
  "attribute": {
    "layer_type": "element_wise_add_layer",

  }
}
base_softmax={
  "type": "base",
  "name": "base_5",
  "attribute": {
    "layer_type": "softmax_layer",

    "attribute": {
		"dim":"1"
    }
  }

}
base_linear={
  "type": "base",
  "name": "base_6",
  "attribute": {
    "layer_type": "linear_layer",

    "attribute": {
		"in_channel":"1",
		"out_channel":"2"
    }
  }

}
base_conv={
  "type": "base",
  "name": "base_7",
     "attribute": {
      "layer_type": "conv_layer",
      "attribute": {
	  "layer_type":"conv",
	  "attribute": {
	  
        "type": "1d",
        "in_channel":"1",
		"out_channel":"2",
		"kernel_size":"3",
		"stride":"1",
		"padding":"0"
      }
    }
}
}
base_act={
  "type": "base",
  "name": "base_8",
     "attribute": {
      "layer_type": "activation_layer",
      "attribute": {
        "layer_type":"leaky relu",
		"attribute":{
		"negative_slope":"0.001"
      }
    }
}
}
base_RNN={
  "type": "base",
  "name": "base_9",
     "attribute": {
      "layer_type": "RNN_layer",
      "attribute": {
		"input_size":"5",
		"hidden_size":"10",
		"num_layers":"20",
		"nonlinearity":"tanh"
    }
}
}
base_LSTM={
  "type": "base",
  "name": "base_10",
     "attribute": {
      "layer_type": "LSTM_layer",
      "attribute": {
		"input_size":"5",
		"hidden_size":"10",
		"num_layers":"20"
    }
}
}
base_norm={
  "type": "base",
  "name": "base_10",
     "attribute": {
      "layer_type": "norm_layer",
      "attribute": {
		"layer_type":"batch_norm",
		"attribute":{
		"type":"1d",
		"num_features":"4"
    }
	}
}
}
modulelist1={
  "type": "modulelist",
  "name": "ml1",
  "attribute": {
    "canvas1": base_norm,
    "num": '10'
  }
}
moduledict1={
  "type": "moduledict",
  "name": "dict1",
  "attribute": {
    "default": "canvas_1",
    "choose": "canvas_2",
    "nets": {
      "canvas_1": base_linear,
      "canvas_2": base_RNN
    }
  }
}
sequential2={
  "type": "sequential",
  "name": "sequential2",
  "attribute": {
    "in": "canvas_1",
    "out": "canvas_13",
    "nets": {
      "canvas_1": base_start,
      "canvas_2": base_view,
	  "canvas_3":base_concate,
	  "canvas_4":base_act,
	  "canvas_5":base_element,
      "canvas_6":base_conv,
      "canvas_7":base_conv,
      "canvas_8":base_softmax,
      "canvas_9":base_RNN,
      "canvas_10":base_LSTM,
      "canvas_11":base_linear,
      "canvas_12":base_norm,
      "canvas_13":base_end
    }
	},
    "nets_conn": [
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
         },
		                {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_5"
             }
         }  ,		                {
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_6"
             }
         },		                {
             "source": {
                "id": "canvas_6"
             },
             "target": {
                 "id": "canvas_7"
             }
         } ,		                {
             "source": {
                "id": "canvas_7"
             },
             "target": {
                 "id": "canvas_8"
             }
         },
             {
             "source": {
                "id": "canvas_8"
             },
             "target": {
                 "id": "canvas_9"
             }
         },
             		                {
             "source": {
                "id": "canvas_9"
             },
             "target": {
                 "id": "canvas_10"
             }
         },		{
             "source": {
                "id": "canvas_10"
             },
             "target": {
                 "id": "canvas_11"
             }
         },
                {
             "source": {
                "id": "canvas_11"
             },
             "target": {
                 "id": "canvas_12"
             }
         },		                {
             "source": {
                "id": "canvas_12"
             },
             "target": {
                 "id": "canvas_13"
             }
         }
    ]
  
}
sequential3={
  "type": "sequential",
  "name": "sequential3",
  "attribute": {
    "in": "canvas_1",
    "out": "canvas_10",
    "nets": {
      "canvas_1": base_start,
      "canvas_2": modulelist1,
	  "canvas_3":moduledict1,
	  "canvas_4":base_act,
      "canvas_5":sequential2,
      "canvas_7":base_concate,
      "canvas_8":base_element,
      "canvas_9":base_element,
	  "canvas_10":base_end
    }
	},
    "nets_conn": [
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
         },
		                {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_5"
             }
         }   ,
              {
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_7"
             }
         } ,   {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_7"
             }
         } ,{
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_8"
             }
         },{
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_8"
             }
         },{
             "source": {
                "id": "canvas_7"
             },
             "target": {
                 "id": "canvas_9"
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
         }
    ]
  
}