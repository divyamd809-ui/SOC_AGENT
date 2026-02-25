async function analyzeLog() {

    const log = document.getElementById("logInput").value;

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ log: log })
    });

    const data = await response.json();

    document.getElementById("totalLogs").innerText = 1;
    document.getElementById("threatCount").innerText = data.threats_detected.length;
    document.getElementById("riskLevel").innerText = data.risk_level;

    document.getElementById("resultBox").innerHTML = `
        <p><strong>Normalized Log:</strong> ${data.normalized_log}</p>
        <p><strong>Threats:</strong> ${data.threats_detected.join(", ") || "None"}</p>
        <p><strong>Attack Type:</strong> ${data.attack_type}</p>
        <p><strong>Risk Level:</strong> ${data.risk_level}</p>
    `;
}