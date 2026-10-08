import urllib.parse

def create_whatsapp_message_link(phone_number, message):
    """
    Creates a WhatsApp message link for an unsaved number.
    Handles country codes and URL encoding.
    """
    # Ensure phone number starts with country code, if not provided, default to a common one or raise error.
    # For simplicity, this example assumes the user provides the full number with country code.
    # A more robust solution would involve a library to parse and validate phone numbers.

    # URL-encode the message to handle spaces and special characters
    encoded_message = urllib.parse.quote(message)

    # Construct the WhatsApp URL
    # The format is https://wa.me/<number>?text=<urlencodedtext>
    # The number should be in international format without any zeros, brackets or dashes, or plus signs.
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    return whatsapp_url

if __name__ == "__main__":
    # Example Usage:
    # Replace with a valid phone number including country code (e.g., +905XXXXXXXXX for Turkey)
    # For demonstration, using a placeholder. In a real Android app, you'd get this from user input.
    target_phone_number = "905551234567"  # Example Turkish number
    message_to_send = "Merhaba, bu kaydedilmemiş bir numaradan gönderilen bir test mesajıdır."

    # Generate the link
    message_link = create_whatsapp_message_link(target_phone_number, message_to_send)

    print(f"Telefon Numarası: {target_phone_number}")
    print(f"Mesaj: {message_to_send}")
    print(f"Oluşturulan WhatsApp Linki: {message_link}")

    # In an Android app, you would then use an Intent to open this URL:
    # val intent = Intent(Intent.ACTION_VIEW)
    # intent.data = Uri.parse(message_link)
    # startActivity(intent)

    print("\nBu Python betiği, WhatsApp mesaj linki oluşturma mantığını gösterir.")
    print("Android uygulamanızda bu linki Intent ile açarak kullanabilirsiniz.")
