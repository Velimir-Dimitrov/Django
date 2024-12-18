document.addEventListener("DOMContentLoaded", () => {
    const faqForm = document.getElementById("faq-form");
    const faqList = document.getElementById("faq-list");
    const faqIdField = document.getElementById("faq-id");
    const questionField = document.getElementById("question");
    const answerField = document.getElementById("answer");

    const API_URL = "/faq/api/";

    // Fetch and display FAQs
    async function loadFAQs() {
        faqList.innerHTML = ""; // Clear the list
        const response = await fetch(API_URL);
        const faqs = await response.json();

        faqs.forEach(faq => {
            const li = document.createElement("li");
            li.innerHTML = `
                <strong>${faq.question}</strong>
                <p>${faq.answer}</p>
                <button onclick="editFAQ(${faq.id}, '${faq.question}', '${faq.answer}')">Edit</button>
                <button onclick="deleteFAQ(${faq.id})">Delete</button>
            `;
            faqList.appendChild(li);
        });
    }

    // Handle form submission
    faqForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const id = faqIdField.value;
        const question = questionField.value;
        const answer = answerField.value;

        const method = id ? "PUT" : "POST";
        const url = id ? `${API_URL}${id}/` : API_URL;

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;


        await fetch(url, {
            method,
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ question, answer }),
        });

        faqForm.reset();
        faqIdField.value = ""; // Clear the hidden field
        loadFAQs();
    });

    // Edit FAQ
    window.editFAQ = (id, question, answer) => {
        faqIdField.value = id;
        questionField.value = question;
        answerField.value = answer;
    };

    // Delete FAQ
    window.deleteFAQ = async (id) => {
        await fetch(`${API_URL}${id}/`, { method: "DELETE" });
        loadFAQs();
    };

    // Initial load
    loadFAQs();
});
