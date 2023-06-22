def savenewimage():
    import requests
    import os

    # Safebooru API endpoint and parameters
    api_url = "https://safebooru.org/index.php"
    params = {
        "page": "dapi",
        "s": "post",
        "q": "index",
        "tags": "yuri",
        "limit": "1",
        "json": "1"
    }

    # Make a request to the Safebooru API
    response = requests.get(api_url, params=params)
    data = response.json()

    # Check if the response contains any results
    if len(data) > 0:
        # Extract the image URL from the API response
        if "image" in data[0]:
            image_url = "https://safebooru.org/images/" + \
                data[0]["directory"] + "/" + data[0]["image"]

            # Create the 'img' directory if it doesn't exist
            directory = "img"
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Determine the next image file number
            file_number = len(os.listdir(directory)) + 1

            # Construct the file path with the image number
            file_name = f"{directory}/{file_number}.jpg"

            # Download the image
            image_data = requests.get(image_url).content

            # Save the image locally with the desired file name
            with open(file_name, "wb") as image_file:
                image_file.write(image_data)

            print(f"Image {file_number}.jpg was downloaded")
        else:
            print("Image URL not found in API response.")
    else:
        print("No images found for the specified search parameters.")


savenewimage()
