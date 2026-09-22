"""from voice_of_patient import transcribe_patient_voice
from brain_of_doc_groq import brain_of_the_doctor
from voice_doc import convert_text_to_doctor_audio, play_audio
import gradio as gr 

import gradio as gr

# Logic + UI

def process_inputs(audio_filepath, image_filepath, video_filepath):
    patient_text = transcribe_patient_voice(audio_filepath)

    doctor_text = brain_of_the_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        video_filepath=video_filepath,
    )

    doctor_audio = convert_text_to_doctor_audio(doctor_text)

    play_audio(doctor_audio)

    return patient_text, doctor_text, str(doctor_audio)

# Play audio for the patient

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(
            sources=["microphone", "upload"],
            type="filepath",
            label="Patient Voice",
        ),
        gr.Image(
            type="filepath",
            label="Patient Image",
        ),
        gr.Video(
            label="Patient Video",
        ),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice"),
    ],
    title="AI Doctor with Vision and Voice",
)

iface.launch()"""
from voice_of_patient import transcribe_patient_voice
from brain_of_doc_groq import brain_of_the_doctor
from voice_doc import convert_text_to_doctor_audio, play_audio
import gradio as gr

# ----------------------------------------------------------------------------
# Logic (unchanged from your original file)
# ----------------------------------------------------------------------------

def process_inputs(audio_filepath, image_filepath, video_filepath):
    patient_text = transcribe_patient_voice(audio_filepath)

    doctor_text = brain_of_the_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        video_filepath=video_filepath,
    )

    doctor_audio = convert_text_to_doctor_audio(doctor_text)

    play_audio(doctor_audio)

    # Also return a "status ready" flag we use to flip the badge text
    return patient_text, doctor_text, str(doctor_audio), "● AI Triage Completed"


def reset_fields():
    return None, None, None, "", "", None, "● Online / Ready"


# ----------------------------------------------------------------------------
# Custom CSS — dark header, light page background, white "cards" with a
# dark title bar, badge pills, status dots. Mirrors the target screenshot.
# ----------------------------------------------------------------------------

CUSTOM_CSS = """
:root {
    --brand-navy: #111827;
    --brand-blue: #2563eb;
    --brand-blue-light: #eaf1ff;
    --brand-green: #16a34a;
    --page-bg: #eef2f9;
    --card-bg: #ffffff;
}

body, .gradio-container {
    background: var(--page-bg) !important;
}

/* ---------- Top navbar ---------- */
#topbar {
    background: var(--brand-navy);
    border-radius: 14px;
    padding: 14px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #fff;
    margin-bottom: 18px;
}
#topbar h1 {
    font-size: 17px;
    margin: 0;
    color: #fff;
}
#topbar p {
    font-size: 12px;
    margin: 0;
    color: #9ca3af;
}
.status-pill {
    background: rgba(255,255,255,0.08);
    color: #6ee7b7;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}

/* ---------- Hero / title card ---------- */
#hero {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
#hero h2 {
    font-size: 30px;
    font-weight: 800;
    margin: 0 0 6px 0;
    color: var(--brand-navy);
}
#hero p {
    color: #6b7280;
    margin: 0 0 14px 0;
}
.badge-row span {
    display: inline-block;
    background: var(--brand-blue-light);
    color: var(--brand-blue);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 20px;
    margin-right: 8px;
}

/* ---------- Section cards (Patient Input / Doctor Response) ---------- */
.section-card {
    background: var(--card-bg);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    padding-bottom: 14px;
}
.card-header {
    background: var(--brand-navy);
    color: #fff;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.card-header h3 {
    margin: 0;
    font-size: 19px;
    color: #fff;
}
.card-header .tag {
    background: rgba(110,231,183,0.15);
    color: #6ee7b7;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 14px;
}
.card-header.green .tag {
    background: rgba(96,165,250,0.15);
    color: #93c5fd;
}
.card-body {
    padding: 16px 20px 0 20px;
}

/* Field group label styling */
.field-label {
    font-weight: 600;
    font-size: 13px;
    color: #374151;
    margin: 10px 0 4px 2px;
}

#analyze-btn {
    background: var(--brand-blue) !important;
    color: #fff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    height: 46px;
}

#reset-btn {
    background: transparent !important;
    color: #dc2626 !important;
    border: none !important;
    font-size: 12px !important;
}

/* ---------- Footer status bar ---------- */
#statusbar {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 10px 18px;
    margin-top: 10px;
    font-size: 12px;
    color: #6b7280;
    display: flex;
    gap: 22px;
}
#statusbar .dot {
    color: #16a34a;
}
"""

# ----------------------------------------------------------------------------
# UI
# ----------------------------------------------------------------------------

with gr.Blocks(css=CUSTOM_CSS, title="AI Skin Specialist") as iface:

    # Top navbar
    gr.HTML(
        """
        <div id="topbar">
            <div>
                <h1>🩺 AI Skin Specialist</h1>
                <p>AI Dermatological Triage &amp; Consultation</p>
            </div>
            <div class="status-pill" id="status-pill-text">● Online / Ready</div>
        </div>
        """
    )

    # Hero / title card
    gr.HTML(
        """
        <div id="hero">
            <h2>AI Skin Specialist</h2>
            <p>Voice, image, and video-assisted multimodal dermatological triage.</p>
            <div class="badge-row">
                <span>v2.4 Clinical AI</span>
                <span>HIPAA Inspired</span>
                <span>Instant AI Multimodal Triage</span>
            </div>
        </div>
        """
    )

    with gr.Row(equal_height=False):

        # ---------------- Patient Input (left) ----------------
        with gr.Column(scale=1, elem_classes="section-card"):
            gr.HTML(
                '<div class="card-header"><h3>🩺 Patient Input</h3>'
                '<span class="tag">Step 1 &amp; 2</span></div>'
            )
            with gr.Column(elem_classes="card-body"):
                gr.HTML('<div class="field-label">🎙️ Describe your skin concern</div>')
                audio_input = gr.Audio(
                    sources=["microphone", "upload"],
                    type="filepath",
                    label=None,
                    show_label=False,
                )

                gr.HTML('<div class="field-label">📷 Upload Skin Image</div>')
                image_input = gr.Image(
                    type="filepath",
                    label=None,
                    show_label=False,
                )

                gr.HTML('<div class="field-label">🎥 Upload Short Video (optional)</div>')
                video_input = gr.Video(
                    label=None,
                    show_label=False,
                )

                analyze_btn = gr.Button(
                    "Analyze Skin (Synthesize Multimodal Triage)",
                    elem_id="analyze-btn",
                )
                reset_btn = gr.Button("↺ Reset All Fields", elem_id="reset-btn")

        # ---------------- Doctor Response (right) ----------------
        with gr.Column(scale=1, elem_classes="section-card"):
            gr.HTML(
                '<div class="card-header green"><h3>📋 Doctor Response</h3>'
                '<span class="tag" id="ai-ready-tag">AI Ready</span></div>'
            )
            with gr.Column(elem_classes="card-body"):
                gr.HTML('<div class="field-label">📝 Speech to Text (ASR)</div>')
                speech_to_text_output = gr.Textbox(
                    show_label=False,
                    lines=4,
                    placeholder="Transcribed patient description will appear here…",
                )

                gr.HTML('<div class="field-label">🩺 Doctor\'s Diagnostic Assessment</div>')
                doctor_response_output = gr.Textbox(
                    show_label=False,
                    lines=8,
                    placeholder="AI diagnostic assessment will appear here…",
                )

                gr.HTML('<div class="field-label">🔊 Doctor\'s Voice Consultation</div>')
                doctor_audio_output = gr.Audio(show_label=False)

    # Footer status bar
    status_html = gr.HTML(
        """
        <div id="statusbar">
            <span><span class="dot">●</span> AI Engine Status: Active</span>
            <span>Gradio: Connected</span>
        </div>
        """
    )

    # ------------------------------------------------------------------
    # Wiring
    # ------------------------------------------------------------------
    status_pill_state = gr.State("● Online / Ready")

    analyze_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input, video_input],
        outputs=[
            speech_to_text_output,
            doctor_response_output,
            doctor_audio_output,
            status_pill_state,
        ],
    )

    reset_btn.click(
        fn=reset_fields,
        inputs=[],
        outputs=[
            audio_input,
            image_input,
            video_input,
            speech_to_text_output,
            doctor_response_output,
            doctor_audio_output,
            status_pill_state,
        ],
    )

iface.launch()