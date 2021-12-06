import torch
import unittest

from super_gradients.training.models import ShelfNet18, ShelfNet34, ShelfNet50, ShelfNet101


class TestShelfNet(unittest.TestCase):
    def test_shelfnet_creation(self):
        """
        test_shelfnet_creation - Tests the creation of the model class itself
            :return:
        """
        dummy_input = torch.randn(1, 3, 512, 512)

        shelfnet18_model = ShelfNet18(classes_num=21)
        # VALIDATES INNER CONV LIST WAS INITIALIZED CORRECTLY
        self.assertTrue(shelfnet18_model.conv_out_list)

        shelfnet34_model = ShelfNet34(classes_num=21)
        # VALIDATES INNER CONV LIST WAS INITIALIZED CORRECTLY
        self.assertTrue(shelfnet34_model.conv_out_list)

        shelfnet50_model = ShelfNet50(classes_num=21)
        # VALIDATES INNER CONV LIST WAS INITIALIZED CORRECTLY
        self.assertTrue(shelfnet50_model.conv_out_list)

        shelfnet101_model = ShelfNet101(classes_num=21)
        # VALIDATES INNER CONV LIST WAS INITIALIZED CORRECTLY
        self.assertTrue(shelfnet101_model.conv_out_list)

        for model in [shelfnet18_model, shelfnet34_model, shelfnet50_model, shelfnet101_model]:
            model.eval()
            with torch.no_grad():
                output = model(dummy_input, aux=False)
                self.assertIsNotNone(output)


if __name__ == '__main__':
    unittest.main()