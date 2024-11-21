system_prompt_candidate = f"""
Analyze the candidate's resume step by step, retrieving accurate and explicit information as presented. If the information is missing or incomplete, leave the field blank. Use the following structure for a precise and concise output:

#### Candidate Details
1. **Name**: Extract the full name from the resume.
2. **Contact Information**: Include phone number and email as listed in the resume.

#### Educational Qualifications
- **Degree**: Format each entry as follows:
  *Degree - School/University/Organization - GPA (if available) - Year of Graduation (if available)*.
- If multiple degrees exist, list them in chronological order, from the earliest to the most recent.

#### Work Experience
- Extract **job titles**, **companies/organizations**, and **tenure (start and end dates)**.
- Format each entry: *Job Title - Company/Organization - Start Date to End Date (or Present)*, followed by a bullet-pointed list of responsibilities.

#### Technical Skills
- List all technologies, tools, programming languages, frameworks, or platforms explicitly mentioned in the resume.
- Avoid broad categories like "software development" unless no specifics are provided.

#### Responsibilities
- Extract task-based and project-based descriptions that detail what the candidate contributed to their roles. Include metrics or outcomes when mentioned.

#### Certificates and Training
- List all certifications or training programs, including the issuing organization and year (if available).

#### Soft Skills
- Deduce soft skills from the resume (e.g., leadership, communication, teamwork, problem-solving). Explicitly state if the candidate has language proficiencies.

#### Additional Information
- Include any extracurricular activities, volunteer work, or notable achievements if explicitly listed.

Provide all responses in a structured format with clear sections. Avoid assumptions and limit inference to what is explicitly supported by the resume.
"""

fn_candidate_analysis = [
    {
        "name": "AnalyzeCV",
        "description": "Analyze candidate resume to get informations.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_name": {
                    "type": "string",
                    "description": "Name of the candidate."
                },
                "phone_number": {
                    "type": "string",
                    "description": "Phone number of the candidate."
                },
                "email": {
                    "type": "string",
                    "description": "Email of candidate. e.g. jackey@gmail.com, hinata@outlook.com"
                },
                "degree": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Educational qualifications. e.g., Bachelor's degree in Computer Science - FPT University - 2024"
                },
                "experience": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Extract **job titles**, **companies/organizations**, and **tenure (start and end dates)**."
                },
                "technical_skill": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List all technologies, tools, programming languages, frameworks, or platforms explicitly mentioned in the resume."
                },
                "responsibility": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Extract task-based and project-based descriptions that detail what the candidate contributed to their roles. Include metrics or outcomes when mentioned."
                },
                "certificate": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Certificates achieved. e.g., Advanced Data Analysis, Basic SQL."
                },
                "soft_skill": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Deduce soft skills from the resume (e.g., leadership, communication, teamwork, problem-solving). Explicitly state if the candidate has language proficiencies."
                },
                "additional_information": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "description": "The category or type of additional information. For example: Membership, Hobbies, Wellness Activities, Volunteer Experience."
                            },
                            "details": {
                                "type": "string",
                                "description": "Specific details or descriptions related to the category. For example: Member of university's Honor Society, Yoga, Skiing, or Literature."
                            }
                        },
                        "required": ["category", "details"]
                    },
                    "description": "Include any additional information about the candidate, such as extracurricular activities, hobbies, wellness activities, interests, volunteer work, or notable achievements."
                },
                "job_recommended": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Recommend what jobs the candidate should apply. e.g. Fullstack Web Developer, Python Developer, AI Engineer, Data Analytics."
                }
            },
            "required": [
                "candidate_name",
                "phone_number",
                "email",
                "degree",
                "experience",
                "technical_skill",
                "responsibility",
                "certificate",
                "soft_skill",
                "additional_information",
                "job_recommended"
            ]
        }
    }
]
