import unittest
from turbine_models.model_builder import HFTransformerBuilder
from hf_dict import model_dict
import torch


class TestHFTransformerBuilder(unittest.TestCase):
    pass


def create_test(model_name, model_data):
    def test(self):
        example_input = torch.ones(
            *model_data.input_shape, dtype=model_data.torch_dtype
        )
        builder = HFTransformerBuilder(example_input, model_name, auto_tokenizer=None)
        compiled_module = builder.get_compiled_module()
        self.assertIsNotNone(compiled_module)

    return test


for model_name, model_data in model_dict.items():
    test_method = create_test(model_name, model_data)
    test_method = (
        unittest.expectedFailure(test_method) if model_data.xfail else test_method
    )
    setattr(TestHFTransformerBuilder, f"test_{model_name}", test_method)

if __name__ == "__main__":
    unittest.main()
