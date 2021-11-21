PROFILE_PHOTO_DIR: str = "/assets/profile_photos/"


class Profile:
    """ A Profile object contains personally identifiable information that is associated with any user. """
    profile_photo_path: str = None
    # path to this user's profile photo
    email: str = None
    # mutable and initialized at registration
    age: int = None
    # the age of the user in years

    def __init__(self):
        pass


class User:
    user_name: str = None
    # mutable and initialized at registration
    UUID: int = None
    # Universally Unique Identifier, immutable and initialized at registration
    profile: Profile = None

    def __init__(self):
        pass
