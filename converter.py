import tfcoreml as tf_converter
tf_converter.convert(tf_model_path = './yoker.pb',
                     mlmodel_path = './yoker.mlmodel',
                     output_feature_names = ['import/save/RestoreV2:0'])
