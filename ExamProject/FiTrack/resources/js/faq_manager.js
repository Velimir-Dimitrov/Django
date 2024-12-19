document.addEventListener("DOMContentLoaded", () => {
    const faqForm = document.getElementById("faq-form");
    const faqList = document.getElementById("faq-list");
    const faqIdField = document.getElementById("faq-id");
    const questionField = document.getElementById("question");
    const answerField = document.getElementById("answer");
    const csrfTokenField = document.getElementById("csrf-token"); // Get the hidden CSRF token field

    const API_URL = "/faq/api/";

    // Function to get CSRF token from hidden field
    function getCSRFToken() {
        return csrfTokenField.value;
    }

    // Fetch and display FAQs
    async function loadFAQs() {
        faqList.innerHTML = ""; // Clear the list
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error("Failed to fetch FAQs");

            const faqs = await response.json();
            faqs.forEach((faq) => {
                const li = document.createElement("li");
                li.dataset.id = faq.id;
                li.innerHTML = `
                    <strong>${faq.question}</strong>
                    <p>${faq.answer}</p>
                    ${USER_IS_SUPERUSER ? `
                    <button class="edit-faq">Edit</button>
                    <button class="delete-faq">Delete</button>
                ` : ''}`
                faqList.appendChild(li);
            });
        } catch (error) {
            console.error("Error loading FAQs:", error);
        }
    }

    // Handle form submission
    faqForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const id = faqIdField.value;
        const question = questionField.value.trim();
        const answer = answerField ? answerField.value.trim() : "";

        if (!question) {
            alert("Please submit your question");
            return;
        }

        const method = id ? "PUT" : "POST";
        const url = id ? `${API_URL}${id}/` : API_URL;

        try {
            const csrfToken = getCSRFToken(); // Get CSRF token
            const response = await fetch(url, {
                method,
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({ question, answer }),
            });

            if (!response.ok) throw new Error("Failed to save FAQ");

            faqForm.reset();
            faqIdField.value = ""; // Clear the hidden field
            loadFAQs();
        } catch (error) {
            console.error("Error saving FAQ:", error);
            alert("An error occurred while saving the FAQ.");
        }
    });

    // Edit FAQ
    faqList.addEventListener("click", (e) => {
        if (e.target.classList.contains("edit-faq")) {
            const li = e.target.closest("li");
            const id = li.dataset.id;
            const question = li.querySelector("strong").textContent;
            const answer = li.querySelector("p").textContent;

            faqIdField.value = id;
            questionField.value = question;
            answerField.value = answer;
        }
    });

    // Delete FAQ
    faqList.addEventListener("click", async (e) => {
        if (e.target.classList.contains("delete-faq")) {
            const li = e.target.closest("li");
            const id = li.dataset.id;

            if (confirm("Are you sure you want to delete this FAQ?")) {
                try {
                    const csrfToken = getCSRFToken(); // Get CSRF token
                    const response = await fetch(`${API_URL}${id}/`, {
                        method: "DELETE",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": csrfToken,
                        },
                    });

                    if (!response.ok) throw new Error("Failed to delete FAQ");

                    loadFAQs(); // Reload the FAQ list after deletion
                } catch (error) {
                    console.error("Error deleting FAQ:", error);
                    alert("An error occurred while deleting the FAQ.");
                }
            }
        }
    });

    // Initial load
    loadFAQs();
});

