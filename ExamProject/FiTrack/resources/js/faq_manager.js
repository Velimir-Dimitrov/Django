document.addEventListener("DOMContentLoaded", async () => {
    const faqForm = document.getElementById("faq-form");
    const faqList = document.getElementById("faq-list");
    const faqIdField = document.getElementById("faq-id");
    const questionField = document.getElementById("question");
    const answerField = document.getElementById("answer");
    const csrfTokenField = document.getElementById("csrf-token"); // CSRF token hidden field

    const API_URL = "/faq/api/";

    function getCSRFToken() {
        return csrfTokenField.value;
    }

    async function loadFAQs() {
        faqList.innerHTML = ""; // Clear the list
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error("Failed to fetch FAQs");

            const faqs = await response.json();

            faqs.forEach((faq) => {
                const li = document.createElement("li");
                li.dataset.id = faq.id;

                const question = document.createElement("strong");
                question.textContent = faq.question;

                const answer = document.createElement("p");
                answer.textContent = faq.answer || "";

                li.appendChild(question);
                li.appendChild(answer);

                if (USER_IS_SUPERUSER) {
                    const editButton = document.createElement("button");
                    editButton.textContent = "Edit";
                    editButton.classList.add("edit-faq");
                    editButton.addEventListener("click", () => editFAQ(faq));

                    const deleteButton = document.createElement("button");
                    deleteButton.textContent = "Delete";
                    deleteButton.classList.add("delete-faq");
                    deleteButton.addEventListener("click", () => deleteFAQ(faq.id));

                    li.appendChild(editButton);
                    li.appendChild(deleteButton);
                }

                faqList.appendChild(li);
            });
        } catch (error) {
            console.error("Error loading FAQs:", error);
        }
    }

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
                body: JSON.stringify({question, answer}),
            });

            if (!response.ok) throw new Error("Failed to save FAQ");

            faqForm.reset();
            faqIdField.value = "";
            await loadFAQs();
        } catch (error) {
            console.error("Error saving FAQ:", error);
            alert("An error occurred while saving the FAQ.");
        }
    });

    function editFAQ(faq) {
        faqIdField.value = faq.id;
        questionField.value = faq.question;
        if (answerField) answerField.value = faq.answer || "";
    }

    async function deleteFAQ(id) {
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

                await loadFAQs();
            } catch (error) {
                console.error("Error deleting FAQ:", error);
                alert("An error occurred while deleting the FAQ.");
            }
        }
    }

    await loadFAQs();
});
