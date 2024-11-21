system_prompt_strength = f"""
    Analyze the candidate's CV to identify their strengths, areas of improvement, and job recommendations. Focus on key strengths in areas such as technical skills, leadership, communication, and adaptability. Provide a brief but comprehensive breakdown of:
    
    - Key Skills (core competencies)
    - Notable Achievements (accomplishments)
    - Leadership/Collaboration
    - Problem Solving/Innovation
    - Communication Skills
    - Analytical Skills
    - Adaptability and Learning
    - Client/Customer Focus
    
    The recommended job roles should align with the strengths, and areas of improvement should help the candidate focus on skill gaps. Use singular pronouns (e.g., "he," "she," or "the candidate").
"""


fn_strength_analysis = [
    {
        "name": "AnalyzeCV",
        "description": "Analyze the candidate's resume for strengths, areas for improvement, and recommended job roles.",
        "parameters": {
            "type": "object",
            "properties": {
                "strengths": {
                    "type": "object",
                    "properties": {
                        "core_competencies": {"type": "string", "description": "Key skills relevant to the candidate's field."},
                        "accomplishments": {"type": "string", "description": "Notable achievements or successful projects."},
                        "leadership_and_collaboration": {"type": "string", "description": "Experience in leadership or teamwork."},
                        "problem_solving_and_innovation": {"type": "string", "description": "Examples of problem-solving or innovative solutions."},
                        "communication_skills": {"type": "string", "description": "Ability to communicate with stakeholders effectively."},
                        "analytical_skills": {"type": "string", "description": "Ability to analyze data and make decisions."},
                        "adaptability_and_learning": {"type": "string", "description": "Ability to learn and adapt to new situations."},
                        "client_and_customer_focus": {"type": "string", "description": "Experience with clients or customers."}
                    },
                    "description": "Candidate's strengths in key areas."
                },
                "areas_of_improvement": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Skills the candidate can improve."
                },
                "job_recommended": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Job roles that match the candidate's profile."
                }
            },
            "required": ["strengths", "areas_of_improvement", "job_recommended"]
        }
    }
]


system_prompt_weakness = f"""
Let's carefully analyze the candidate's resume for specific weaknesses and areas for improvement. For each category, provide detailed feedback, and if certain information isn't detected, suggest what could be added to improve the resume. Fill in the following fields:

1. **Skills and Qualifications**:
   - Identify any missing or outdated skills relevant to the candidate's field. Suggest certifications if relevant.

   "missing_skills": If no missing skills are detected, provide suggestions for enhancing the skills list.
   "outdated_skills": Highlight any outdated skills or technologies.
   "relevant_certifications": Recommend any certifications the candidate could pursue.

2. **Impact and Achievements**:
   - Review the resume for measurable accomplishments, like KPIs, and provide specific suggestions to add quantifiable achievements if missing.

   "impact_and_achievements": If the candidate lacks quantifiable achievements, suggest examples such as "Improved sales by 20%," or "Reduced costs by 10%."

3. **Clarity of Descriptions**:
   - Examine the clarity of responsibilities and projects described in the resume.

   "vague_responsibilities": Highlight vague or unclear job responsibilities. Suggest adding more specific details where needed.
   "vague_projects": Point out any project descriptions that lack details or context. Provide suggestions for improvement.

4. **Leadership and Collaboration**:
   - Determine whether leadership and teamwork examples are well represented.

   "leadership_and_collaboration": If leadership and teamwork examples are lacking, suggest how the candidate can demonstrate these traits, even if through side projects or volunteer work.

5. **Career Trajectory**:
   - Analyze for job-hopping or employment gaps, and suggest ways to address these concerns.

   "job_hopping": Highlight frequent job changes or career instability if present.
   "employment_gaps": Point out unexplained gaps in employment, and recommend ways to address them.

6. **Resume Formatting**:
   - Identify issues with the structure, format, or missing sections of the resume.

   "formatting_issues": Describe any formatting issues that make the resume difficult to read.
   "missing_sections": Highlight if key sections (like education, skills, or experience) are missing.

For each section, provide actionable suggestions on how the candidate can improve their resume, even if no significant weaknesses are detected.
"""

# """


fn_weakness_detection = [
    {
        "name": "AnalyzeResumeWeaknesses",
        "description": "Generalized analysis of a candidate's resume to identify key weaknesses or areas for improvement.",
        "parameters": {
            "type": "object",
            "properties": {
                "skills_and_qualifications": {
                    "type": "object",
                    "properties": {
                        "missing_skills": {
                            "type": "string",
                            "description": "Skills or qualifications that the candidate lacks, relative to the job or industry requirements.",
                        },
                        "outdated_skills": {
                            "type": "string",
                            "description": "Skills or tools listed that are no longer in demand.",
                        },
                        "relevant_certifications": {
                            "type": "string",
                            "description": "Certifications or formal qualifications missing from the resume that are important for the candidate's field."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Analysis of the candidate's skills and qualifications with suggestions for improvement. Encourage the candidate to gain new skills, update outdated skills, or pursue certifications that can enhance their profile."
                        }
                    },
                },
                "impact_and_achievements": {
                    "type": "object",
                    "properties": {
                        "issue": {
                            "type": "string",
                            "description": "Specific examples where the resume lacks measurable results or accomplishments, such as KPIs or key outcomes from previous roles.",
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Recommend the candidate add measurable achievements, such as 'increased sales by 15%' or 'reduced processing time by 30%.'"
                        }
                    }
                },
                "clarity_of_descriptions": {
                    "type": "object",
                    "properties": {
                        "vague_responsibilities": {
                            "type": "string",
                            "description": "Responsibilities listed that are too general or lack specific detail."
                        },
                        "vague_projects": {
                            "type": "string",
                            "description": "Projects described without sufficient context, tools used, or results achieved."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Analysis of areas where the candidate's descriptions are unclear or lack detail. Encourage the candidate to be more specific about their roles, technologies used, and the impact of their contributions.",
                        }
                    },
                },
                "leadership_and_collaboration": {
                    "type": "object",
                    "properties": {
                        "issue": {
                            "type": "string",
                            "description": "Identify if the candidate lacks evidence of leadership, teamwork, or collaboration experience."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Suggest highlighting teamwork and leadership roles, even if informal, or adding examples of collaboration in various projects."
                        }
                    }
                },
                "career_trajectory": {
                    "type": "object",
                    "properties": {
                        "job_hopping": {
                            "type": "string",
                            "description": "Detect frequent job changes without clear career advancement."
                        },
                        "employment_gaps": {
                            "type": "string",
                            "description": "Gaps in employment history that are not explained or accounted for. If there is no employment gaps detected, then leave it as None"
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Identify issues in the candidate’s career progression or any unexplained employment gaps. Encourage explaining gaps and frequent job changes by framing them positively, such as skill development during breaks or growth achieved through different roles.",
                        }
                    },
                },
                "resume_formatting": {
                    "type": "object",
                    "properties": {
                        "formatting_issues": {
                            "type": "string",
                            "description": "General formatting issues that make the resume difficult to read or understand, such as poor structure or inconsistent use of fonts and spacing."
                        },
                        "missing_sections": {
                            "type": "string",
                            "description": "Important sections that are missing, such as education, skills, or relevant work experience."
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Analysis of formatting or structural problems in the resume. Suggest improving the layout with clear headings, consistent formatting, and ensuring that all key sections (skills, experience, education) are included."
                        }
                    },
                }
            },
            "required": [
                "skills_and_qualifications",
                "impact_and_achievements",
                "clarity_of_descriptions",
                "leadership_and_collaboration",
                "career_trajectory",
                "resume_formatting"
            ]
        }
    }
]