from django.contrib.auth.decorators import user_passes_test


def verified_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def is_verified(user):
        if user.is_verified():
            return True
        return False
    return user_passes_test(is_verified)