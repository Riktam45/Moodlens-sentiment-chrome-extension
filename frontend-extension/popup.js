const analyzeBtn = document.getElementById("analyzeBtn")
const manualBtn = document.getElementById("manualBtn")
const resultsDiv = document.getElementById("results")
const loading = document.getElementById("loading")

analyzeBtn.addEventListener("click", async () => {

    const url = document.getElementById("postUrl").value

    loading.classList.remove("hidden")
    resultsDiv.innerHTML = ""

    try {
        
        const response = await fetch("http://localhost:8000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url })
        })

        const data = await response.json()

        loading.classList.add("hidden")

        displayResults(data)

    } catch (error) {
        loading.classList.add("hidden")
        resultsDiv.innerHTML = "<p>Error analyzing post</p>"
    }
})

manualBtn.addEventListener("click", async () => {

    const comment = document.getElementById("manualComment").value

    try {

        const response = await fetch("http://localhost:8000/manual", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ comment })
        })

        const data = await response.json()

        const result = data.comments[0]

        resultsDiv.innerHTML = `
            <div class="card">
                <h2>${result.sentiment}</h2>
                <p>Confidence: ${result.confidence}%</p>
                <p>${result.comment}</p>
            </div>
        `

    } catch (error) {
        resultsDiv.innerHTML = "<p>Error analyzing comment</p>"
    }
})

function displayResults(data) {

    resultsDiv.innerHTML = `

    <div class="stats">

        <div class="stat-card positive">
            <h2>${data.positive_percentage}%</h2>
            <p>Positive</p>
        </div>

        <div class="stat-card neutral">
            <h2>${data.neutral_percentage}%</h2>
            <p>Neutral</p>
        </div>

        <div class="stat-card negative">
            <h2>${data.negative_percentage}%</h2>
            <p>Negative</p>
        </div>

    </div>

    <div class="total-comments">
        Total Comments: ${data.total_comments}
    </div>

    `
}