import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="MedTech AI",
    page_icon="🔬",
    layout="centered"
)

st.title("🔬 MedTech AI")
st.caption("Educational prototype • Simulated data only")

st.info(
    "This demo analyzes sample readings. "
    "It cannot verify medicine authenticity or safety."
)

st.subheader("Sample Analyzer")

readings_text = st.text_input(
    "Enter readings separated by commas",
    "120, 125, 180, 122, 200"
)

margin = st.slider(
    "Demo threshold margin",
    min_value=5,
    max_value=50,
    value=20
)

if st.button("Analyze readings"):
    try:
        readings = [
            float(value.strip())
            for value in readings_text.split(",")
        ]

        if not readings or any(value < 0 for value in readings):
            st.error("Enter non-negative numbers.")
        else:
            average = sum(readings) / len(readings)
            threshold = average + margin

            st.metric("Average reading", f"{average:.2f}")
            st.metric("Demo threshold", f"{threshold:.2f}")

            results = [
                "Unusual pattern" if value > threshold
                else "Within demo range"
                for value in readings
            ]

            for index, (value, result) in enumerate(
                zip(readings, results), start=1
            ):
                st.write(f"Sample {index}: {value} — {result}")

            fig, ax = plt.subplots()
            ax.bar(range(1, len(readings) + 1), readings)
            ax.axhline(
                threshold,
                linestyle="--",
                label="Demo threshold"
            )
            ax.set_xlabel("Sample")
            ax.set_ylabel("Simulated reading")
            ax.set_title("Sample Reading Analysis")
            ax.legend()
            st.pyplot(fig)
            plt.close(fig)

    except ValueError:
        st.error("Invalid input. Example: 120, 125, 180")
