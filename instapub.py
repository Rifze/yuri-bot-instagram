def publish_to_instagram():
    import os
    from instabot import Bot
    from config import username, password

    # Find the highest numbered image file in the "img" directory
    directory = "img"
    image_files = os.listdir(directory)
    image_files.sort(key=lambda x: int(os.path.splitext(x)[0]))
    highest_numbered_image = image_files[-1]

    # Path to the image file to be published
    image_path = os.path.join(directory, highest_numbered_image)

    # Confirm the image path before publishing
    confirmation = input(
        f"Publish image '{highest_numbered_image}' to Instagram? (y/n): ")

    if confirmation.lower() == "y":
        # Prompt for a caption
        caption = input("Enter the caption for the image: ")

        # Initialize the Instagram bot
        bot = Bot()
        bot.login(username=username, password=password)

        # Publish the image to Instagram with the caption
        bot.upload_photo(image_path, caption=caption)

        # Logout from Instagram
        bot.logout()
        print("Image published successfully.")
    else:
        print("Publishing canceled.")


# Call the function to execute the script
publish_to_instagram()
