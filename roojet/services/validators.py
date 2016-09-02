from plans.validators import ModelCountValidator
from plans.quota import get_user_quota
from models import Product


class ProductValidator(ModelCountValidator):
    """
    Validates that the user websites number
    doesn't conflict with the plan he has acquired
    """
    code = 'NUMBER_OF_PRODUCTS'
    model = Product

    def get_queryset(self, user):
        """
        Queryset contains all the products for a given user
        """
        return self.model.objects.filter(created_by=user)

    def get_quota_value(self, user, quota_dict=None):
        """
        Returns quota value for a given user
        """
        if quota_dict is None and user.userplan.plan is not None:
            quota_dict = get_user_quota(user)
        if quota_dict is not None:
            return quota_dict.get(self.code, None)
        else:
            return None


product_validator = ProductValidator()
