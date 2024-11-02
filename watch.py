import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Pattern to get what is between <iframe(desired url to extract)></iframe>
    httml_pattern = r"<iframe(.*)><\/iframe>"
    # Pattern to get what is after https... using ?P<>
    url_pattern = (
        r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)(?P<video_tag>[a-z_A-Z_0-9]+)"
    )

    # Extract what is between <iframe(desired url to extract)></iframe> and assig it to video_match
    if video_match := re.search(httml_pattern, s):
        # If there is a match, assign it to url variable, else assign None
        url = video_match.group(1) if video_match else None
        # Extract what is after https... and assig it to url_match
        if url_match := re.search(url_pattern, url):
            # If there is a match in group 4 tag it as "video_tag", assign it to video_url variable, else assign None
            video_url = url_match.group("video_tag") if url_match else None

            # Return a useful video url
            return f"https://youtu.be/{video_url}"


if __name__ == "__main__":
    main()
