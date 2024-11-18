from typing import List
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
#from groq import Groq # type: ignore
from openai import OpenAI
import instructor 
from jsonify import convert
from flask import jsonify
#from json_class import QuestionModel

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class QuestionModel(BaseModel):
    question: str
    choices: list[str]
    
class QuestionList(BaseModel):
    title: str
    question_bank: list[QuestionModel]
'''
class OutputModel(BaseModel):
    title = str
    question_bank: list[str]
    def __init__(self,title):
        self.title = title
        self.questions = []

    def add_question(self, question_text, choices):
        question = {
            "question_text": question_text,
            "choices": choices
        }
        self.questions.append(question)
'''

content = "Apple Store Online - Holiday Gifts - Apple (CA) Store. The latest. Only at Apple. The Apple experience. Special stores. Quick Links Footer footnotes Shop and Learn Shop and Learn + Apple Wallet Apple Wallet + Account Account + Entertainment Entertainment + Apple Store Apple Store + For Business For Business + For Education For Education + For Healthcare For Healthcare + Apple Values Apple Values + About Apple About Apple + Customise your Mac and create your own style of Apple Watch. Pay over time with monthly financing. Free extended returns between now and 1.8.25.4 Make them yours. Engrave a mix of emoji, names and numbers for free. Six Apple services. One easy subscription. ∆ Apple Intelligence is available in beta on all iPhone 16 models, iPhone 15 Pro, iPhone 15 Pro Max, iPad mini (A17 Pro), and iPad and Mac models with M1 and later, with Siri and device language set to US English, as part of an iOS 18, iPadOS 18 and macOS Sequoia update. English (Australia, Canada, Ireland, New Zealand, South Africa, UK) language support available this December. Some features, and support for additional languages, like Chinese, English (India, Singapore), French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese and others, will be coming over the course of the next year. ‡ Payment plans available on approved credit for iPhone and Apple Watch purchases over $99, Apple Vision Pro purchases over $99, Mac purchases over $199, and iPad purchases over $199. Offer valid on qualifying purchases of eligible Apple products, at Apple Store locations, apple.com/ca, on the Apple Store app and by calling 1‑800‑MY‑APPLE. Financing provided by Affirm, and all transactions are subject to approval. Financing offers may vary from time to time and may be amended or cancelled at any time. See apple.com/ca/shop/browse/financing for more information. Quebec residents: Learn more about financing here. 7.99% APR Representative example based on $1099 purchase: Total repayment amount of $1,192.79 paid over 24 monthly payments of $49.70 at 7.99% APR. Total interest charges and cost of borrowing $93.79. Example transaction amount does not include applicable taxes, which must be paid in full at time of shipment or pickup. 7.99% APR Representative example based on $1099 purchase: Total repayment amount of $1,192.79 paid over 24 monthly payments of $49.70 at 7.99% APR. Total interest charges and cost of borrowing $93.79. Example transaction amount does not include applicable taxes, which must be paid in full at time of shipment or pickup. * New and qualified returning subscribers only. $12.99/month after free trial. Only one offer per Apple Account and only one offer per family if you’re part of a Family Sharing group, regardless of the number of devices that you or your family purchase. This offer is not available if you or your family have previously accepted an Apple TV+ three-months-free or one-year-free offer. Offer valid for three months after eligible device activation. Plan automatically renews until cancelled. Restrictions and other terms apply. 1. Trade‑in values will vary based on the condition, year and configuration of your eligible trade‑in device. Not all devices are eligible for credit. You must be at least the age of majority to be eligible to trade in for credit or for an Apple Gift Card. Trade‑in value may be applied towards a qualifying new device purchase or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when the estimate was made. Sales tax will be assessed on the full value of a new device purchase. In‑store trade‑in requires presentation of a valid photo ID. Offer may not be available in all stores, and may vary between in‑store and online trade‑in. Some stores may have additional requirements. Apple or its trade‑in partners reserve the right to refuse, cancel or limit the quantity of any trade‑in transaction for any reason. More details are available from Apple’s trade‑in partner for trade‑in and recycling of eligible devices. Restrictions and limitations may apply. 2. Special pricing available to qualified customers. To learn more about how to start qualifying for special pricing, talk to an Apple Specialist in a store or give us a call on 1‑800‑MY‑APPLE. 3. $13.00 two-hour delivery on eligible Apple products in most areas. Offer is not available on customized Mac, engraved products, and for certain order types including orders paid for with financing or by bank transfer. Delivery times vary according to your selected delivery address, availability of your items and the time of day you place your order. Find a store to view local store hours or see checkout for estimated delivery. A signature is required for delivery. Drivers may ask for verbal confirmation of receipt from a safe distance to satisfy the signature requirement. 4. Purchases made by network provider financing are not eligible and subject to standard returns policy. ⁺ New subscribers only. $10.99/month after trial. Offer is available for new Apple Music subscribers with a new eligible device for a limited time only. Offer redemption for eligible audio devices requires connecting or pairing to an Apple device running the latest iOS or iPadOS. Offer redemption for Apple Watch requires connecting or pairing to an iPhone running the latest iOS. Offer good for three months after eligible device activation. Only one offer per Apple Account, regardless of the number of eligible devices you purchase. Plan automatically renews until cancelled. Restrictions and other terms (Opens in a new window) apply. We use your location to show you delivery options faster. We found your location using your IP address or because you entered it during a previous visit to Apple. More ways to shop: Find an Apple Store or other retailer near you. Or call 1‑800‑MY‑APPLE."

def draft_url(content, role='user'):
    return {
        'role': role,
        'content': content
    }


def generate_qna(content):
    messages = [
        {
            "role": "system", 
            "content": "generates 5 questions and multiple-choice options that help categorize users visiting the site"
        }
    ]
    messages.append(draft_url(content))
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=messages,
        response_format=QuestionList,
    )
    output = completion.choices[0].message.parsed
    #print(str(output.title))
    #json_output = OutputModel(str(output.title))
    #for i in range(0, len(output.question_bank)):
    #    json_output.add_question(output.question_bank[i].question, output.question_bank[i].choices)

    return output.question_bank

'''
messages = [
        {
            "role": "system", 
            "content": "generates questions and multiple-choice options that help categorize users visiting the site"
        }
    ]
messages.append(draft_url(content))
completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini-2024-07-18",
    messages=messages,
    response_format=QuestionList,
)
output = completion.choices[0].message.parsed


print(output.question_bank[0].question)
'''
