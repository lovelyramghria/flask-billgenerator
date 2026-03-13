from flask import Flask, request, send_file, render_template, jsonify
from datetime import datetime

import requests
from io import BytesIO
# from models import db, Bill, BillItem

app = Flask(__name__)

# INVOICE_API_URL = "https://invoice-generator.com"  # Official API endpoint
# API_KEY = "sk_yWWIwyXfEqNfSEnTLpu7EH0zY4J1Wq0A"  # Replace with your key


@app.route("/")
def home():
    return render_template("index.html")

# ---------------- INVOICE ROUTE ---------------- #
# @app.route("/generate-invoice", methods=["POST"])
# def generate_invoice():
#     try:
#         data = request.get_json()

#         invoice_payload = {
#             "from": "Lovely Store",
#             "to": "Customer",
#             "number": data["id"],
#             "items": [
#                 {
#                     "name": i["name"],
#                     "quantity": i["quantity"],
#                     "unit_cost": i["price"]
#                 } for i in data["items"]
#             ]
#         }

#         response = requests.post(
#             INVOICE_API_URL,
#             json=invoice_payload
#         )

#         return send_file(
#             BytesIO(response.content),
#             mimetype="application/pdf",
#             as_attachment=False,
#             download_name="invoice.pdf"
#         )

#     except Exception as e:
#         print("ERROR:", e)
#         return {"error": str(e)}, 500

# @app.route("/generate-invoice", methods=["POST"])
# def generate_invoice():
#     try:
#         data = request.get_json()

#         # Call the Invoice Generator API
#         response = requests.post(
#             INVOICE_API_URL,
#             json=data,
#             headers={
#                 "Authorization": f"Bearer {API_KEY}",
#                 "Content-Type": "application/json"
#             }
#         )
#         response.raise_for_status()

#         # Send PDF back to browser
#         return send_file(
#             BytesIO(response.content),
#             mimetype="application/pdf",
#             as_attachment=False,
#             download_name="invoice.pdf"
#         )
#     except Exception as e:
#         return {"error": str(e)}, 500  # ← move inside except


# ✅ ALWAYS LAST
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)



# <!-- invoice pdf logic with api 
# window.deliverBill = function (billId) {
#   const billIndex = savedBills.findIndex(b => b.id === billId);
#   if (billIndex === -1) return alert("Bill not found");
#   const bill = savedBills[billIndex];

#   // ✅ Convert bill → invoice JSON format
#   const invoiceData = {
#     from: `Kahani Swaad Di\nBooth No. 64, Phase 5, Mohali, Punjab\n📞 78892-65130, 97817-70364\n🟢 100% Veg`,
#     to: "Customer",
#     number: String(bill.id),
#     date: new Date(bill.time).toLocaleDateString("en-IN"),
#     items: bill.items.map(i => ({
#       name: i.name,
#       quantity: i.quantity,
#       unit_cost: i.price   // 🔥 convert price → unit_cost
#     })),
#     notes: "Thank you for visiting! 🙏\nPlease come again",
#     terms: "GST: Not Applicable"
#   };
#   fetch("/generate-invoice", {
#     method: "POST",
#     headers: { "Content-Type": "application/json" },
#     body: JSON.stringify(invoiceData),  // 🔥 send formatted JSON
#   })
#   .then(async res => {
#     if (!res.ok) {
#       const err = await res.text();
#       throw new Error(err);
#     }
#     const contentType = res.headers.get("Content-Type") || "";
#     if (!contentType.includes("application/pdf")) {
#       throw new Error("Invoice not generated");
#     }
#     return res.blob();
#   })
#   .then(blob => {
#     const url = window.URL.createObjectURL(blob);
#     window.open(url, "_blank");

#     // Mark delivered
#     savedBills.splice(billIndex, 1);
#     localStorage.setItem("savedBills", JSON.stringify(savedBills));
#     renderSavedBills();
#   })
#   .catch(err => {
#     alert("Delivery failed: " + err.message);
#   });
# }; -->