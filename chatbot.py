import streamlit as st
import random

# Define the generated pairs
pairs = [
     [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatGPT."]
    ],
    [
        r"how are you ?",
        ["I'm good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Apologies accepted"]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I assist you?"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
    [
        r"(.*) (hungry|sleepy|groot)",
        [
            "%1 %2? I'm always here to chat!",
            "Why don't you grab a snack or take a nap?",
            "I am Groot!"
        ]
    ],
    [
        r"tell me a joke",
        ["Sure, here you go: Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"what is your favorite color ?",
        ["I don't have a favorite color as I am a chatbot, but I like all colors!"]
    ],
    [
        r"who created you ?",
        ["I was created by OpenAI, a company focused on artificial intelligence research and development."]
    ],
    [
        r"what can you do ?",
        ["I can assist you with answering questions, providing information, and engaging in conversations."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem! If you have any more questions, feel free to ask."]
    ],
    [
        r"how old are you ?",
        ["I don't have an age as I am an AI-powered chatbot."]
    ],
    [
        r"what is the meaning of life ?",
        ["The meaning of life can vary for each individual. It's a philosophical question that has different interpretations."]
    ],
    ["What is engineering?", "Engineering is the application of scientific and mathematical principles to design, create, and optimize structures, systems, and processes."],
    ["How can engineers contribute to society?", "Engineers can contribute to society by designing and implementing infrastructure, developing life-saving medical technologies, improving transportation systems, enhancing communication networks, and creating technologies that improve the quality of life."],
    ["hi", "Hello! How can I assist you today?"],
    ["hello", "Hi there! How can I help you?"],
    ["how are you", "I'm doing well, thank you. How about you?"],
    ["what's up", "Not much. How can I assist you today?"],
    ["how can you help me", "I can provide information, answer questions, and assist with various topics. Feel free to ask me anything!"],
    ["tell me a joke", "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!"],
    ["thank you", "You're welcome! If you have any more questions, feel free to ask."],
    ["goodbye", "Goodbye! Have a great day!"],
    # Add more pairs here
]
pairs += [
    [
        r"what is engineering ?",
        ["Engineering is the application of scientific and mathematical principles to design, build, and improve structures, machines, systems, and processes."]
    ],
    [
        r"what are the different fields of engineering ?",
        ["There are various fields of engineering, such as civil engineering, mechanical engineering, electrical engineering, chemical engineering, computer engineering, aerospace engineering, and biomedical engineering."]
    ],
    [
        r"what does a civil engineer do ?",
        ["Civil engineers design and supervise the construction of infrastructure projects like buildings, bridges, roads, dams, and water supply systems."]
    ],
    [
        r"what does a mechanical engineer do ?",
        ["Mechanical engineers work with machines, engines, and thermal systems, designing, analyzing, and manufacturing mechanical devices."]
    ],
    [
        r"what does an electrical engineer do ?",
        ["Electrical engineers deal with electrical systems, designing and developing components, devices, and power systems for various applications."]
    ],
    [
        r"what does a chemical engineer do ?",
        ["Chemical engineers apply principles of chemistry and engineering to design and operate processes in industries like pharmaceuticals, chemicals, and energy production."]
    ],
    [
        r"what does a computer engineer do ?",
        ["Computer engineers focus on designing and developing computer hardware and software, including computer systems, networks, and embedded systems."]
    ],
    [
        r"what does an aerospace engineer do ?",
        ["Aerospace engineers design and develop aircraft, spacecraft, satellites, and missiles, ensuring they meet performance, safety, and efficiency requirements."]
    ],
    [
        r"what does a biomedical engineer do ?",
        ["Biomedical engineers combine engineering and medical principles to design and develop medical devices, equipment, and healthcare technologies."]
    ],
    [
        r"how long does it take to become an engineer ?",
        ["It typically takes four to five years to complete a bachelor's degree in engineering. Further specialization or advanced degrees may require additional years of study."]
    ],
    [
        r"what are some famous engineering projects ?",
        ["There are many famous engineering projects, including the Panama Canal, the Hoover Dam, the International Space Station, the Burj Khalifa, and the Golden Gate Bridge."]
    ],
    [
        r"what are the challenges faced by engineers ?",
        ["Engineers face challenges such as ensuring safety, meeting technical requirements, managing costs, adopting sustainable practices, and keeping up with rapidly evolving technology."]
    ],
    [
        r"how is technology shaping the field of engineering ?",
        ["Technology is revolutionizing engineering by enabling advanced simulations, 3D printing, automation, artificial intelligence, and data analytics, leading to more efficient and innovative solutions."]
    ],
    [
        r"what are the emerging trends in engineering ?",
        ["Emerging trends in engineering include renewable energy, autonomous vehicles, artificial intelligence, robotics, virtual reality, and sustainable design and construction practices."]
    ],
    [
        r"how can I become an engineer ?",
        ["To become an engineer, you typically need to earn a bachelor's degree in engineering or a related field. It's also beneficial to gain practical experience through internships and participate in professional engineering organizations."]
    ],
    [
        r"what are the skills needed to be a successful engineer ?",
        ["Some important skills for engineers include problem-solving, critical thinking, creativity, strong technical knowledge, communication skills, teamwork, adaptability, and a lifelong learning mindset."]
    ],
    [
        r"what is the future of engineering ?",
        ["The future of engineering looks promising, with advancements in fields like sustainable energy, biotechnology, nanotechnology, artificial intelligence, smart cities, and space exploration."]
    ],
    [
        r"can engineers contribute to tackling global challenges ?",
        ["Absolutely! Engineers play a crucial role in addressing global challenges such as climate change, pollution, renewable energy adoption, infrastructure development, clean water access, and healthcare advancements."]
    ],
    [
        r"what is the role of ethics in engineering ?",
        ["Ethics are vital in engineering, ensuring professionals adhere to moral principles, prioritize safety, consider societal impact, protect the environment, and maintain professional integrity."]
    ],
    [
        r"what is the difference between an engineer and a scientist ?",
        ["While engineers and scientists both use scientific knowledge, engineers focus on applying that knowledge to create practical solutions and technologies, whereas scientists aim to understand and expand knowledge through research."]
    ],
    [
        r"tell me about some engineering breakthroughs",
        ["Some notable engineering breakthroughs include the development of the internet, the invention of the electric light bulb, the discovery of antibiotics, the creation of the first computer, and the invention of the transistor."]
    ],
    [
        r"what is reverse engineering ?",
        ["Reverse engineering is the process of analyzing and understanding the design and functionality of a product or system in order to recreate, replicate, or improve upon it."]
    ],
    [
        r"what is the role of women in engineering ?",
        ["Women have made significant contributions to engineering throughout history and continue to play a vital role. Efforts are being made to encourage more women to pursue engineering and increase their representation in the field."]
    ],
    [
        r"how does engineering contribute to sustainable development ?",
        ["Engineering contributes to sustainable development by designing eco-friendly buildings, developing renewable energy sources, improving resource efficiency, and implementing sustainable infrastructure and transportation systems."]
    ],
    [
        r"can engineering be a creative profession ?",
        ["Absolutely! Engineering involves creative problem-solving, innovative design, and finding unique solutions to complex challenges, making it a highly creative profession."]
    ],
    [
        r"what are some engineering certifications or licenses ?",
        ["There are various certifications and licenses available for engineers, depending on their specialization and country of practice. Some examples include Professional Engineer (PE), LEED certification for sustainable design, and various software-specific certifications."]
    ],
    [
        r"how can engineers contribute to society ?",
        ["Engineers contribute to society by designing and implementing infrastructure, developing life-saving medical technologies, improving transportation systems, enhancing communication networks, and creating technologies that improve the quality of life."]
    ],
    [
        r"what is the role of innovation in engineering ?",
        ["Innovation is essential in engineering as it drives the development of new technologies, processes, and solutions. Engineers strive to push boundaries, challenge existing norms, and create breakthroughs through innovative thinking."]
    ],
    [
        r"what is the role of mathematics in engineering ?",
        ["Mathematics is fundamental to engineering, providing the tools for analysis, modeling, and problem-solving. Engineers use mathematical principles to design and optimize systems and structures."]
    ],
    [
        r"what is the role of computer programming in engineering ?",
        ["Computer programming is integral to engineering, allowing engineers to develop software, simulate systems, automate processes, and control devices. It plays a vital role in various engineering disciplines."]
    ],
    [
        r"how is engineering contributing to space exploration ?",
        ["Engineering has played a crucial role in space exploration, enabling the design and construction of spacecraft, satellites, rovers, and launch systems, as well as developing life support systems and conducting experiments in microgravity."]
    ],
    [
        r"what is the role of engineering in disaster management ?",
        ["Engineering plays a significant role in disaster management by designing resilient infrastructure, developing early warning systems, creating evacuation plans, and implementing measures to mitigate the impact of natural disasters."]
    ],
    [
        r"what is the impact of engineering on the environment ?",
        ["Engineering has both positive and negative impacts on the environment. While it contributes to environmental challenges, engineers are also working on developing sustainable technologies, renewable energy solutions, and eco-friendly practices to minimize negative impacts."]
    ],
    [
        r"what are some engineering challenges in the 21st century ?",
        ["Engineering faces challenges such as climate change mitigation, renewable energy adoption, urbanization, water scarcity, sustainable transportation, healthcare advancements, and addressing the needs of an increasingly interconnected world."]
    ],
    [
        r"how is engineering revolutionizing healthcare ?",
        ["Engineering is revolutionizing healthcare by developing medical devices, imaging technologies, prosthetics, robotic surgery systems, telemedicine solutions, and personalized healthcare approaches, leading to improved diagnostics, treatments, and patient outcomes."]
    ],
    [
        r"how is engineering helping to solve the global energy crisis ?",
        ["Engineering is playing a crucial role in addressing the global energy crisis by developing renewable energy sources, improving energy efficiency, designing smart grids, and exploring advanced energy storage solutions."]
    ],
    [
        r"what are some ethical considerations in engineering ?",
        ["Ethical considerations in engineering include ensuring safety, minimizing environmental impact, protecting user privacy and data security, considering social and cultural factors, and upholding professional integrity."]
    ],
    [
        r"what is the role of engineers in the development of smart cities ?",
        ["Engineers contribute to the development of smart cities by designing intelligent transportation systems, energy-efficient buildings, sustainable infrastructure, advanced waste management systems, and implementing technologies for data-driven decision-making."]
    ],
    [
        r"what are the emerging technologies in the field of engineering ?",
        ["Emerging technologies in engineering include artificial intelligence, machine learning, Internet of Things (IoT), blockchain, 3D printing, virtual reality, augmented reality, and advanced materials."]
    ],
    [
        r"what is the role of engineering in improving transportation systems ?",
        ["Engineering plays a crucial role in improving transportation systems by designing efficient road networks, developing high-speed railways, creating autonomous vehicles, and implementing smart traffic management systems."]
    ],
    [
        r"how is engineering contributing to sustainable construction practices ?",
        ["Engineering contributes to sustainable construction practices by promoting energy-efficient building designs, using eco-friendly materials, implementing waste reduction strategies, and adopting green building certifications."]
    ],
    [
        r"what is the future of engineering education ?",
        ["The future of engineering education is likely to incorporate more interdisciplinary approaches, hands-on experiential learning, industry collaboration, and integration of emerging technologies to prepare students for the evolving demands of the field."]
    ],
    [
        r"what is the role of engineering in combating climate change ?",
        ["Engineering plays a critical role in combating climate change by developing renewable energy technologies, designing energy-efficient systems, implementing sustainable practices, and promoting environmental awareness."]
    ],
    [
        r"what are the challenges in implementing sustainable engineering practices ?",
        ["Challenges in implementing sustainable engineering practices include resistance to change, high upfront costs, limited awareness and understanding, technological limitations, and the need for policy support and regulations."]
    ],
    [
        r"what are the ethical considerations in artificial intelligence development ?",
        ["Ethical considerations in artificial intelligence development include ensuring transparency, fairness, privacy protection, avoiding bias, accountability, and addressing potential socio-economic impacts."]
    ],
    [
        r"what is the role of engineers in cybersecurity ?",
        ["Engineers play a crucial role in cybersecurity by designing secure systems, developing encryption algorithms, implementing robust network architectures, and constantly updating defenses to protect against cyber threats."]
    ],
    [
        r"how is engineering contributing to water management ?",
        ["Engineering contributes to water management by designing efficient water supply and distribution systems, developing wastewater treatment technologies, implementing water conservation measures, and addressing water scarcity challenges."]
    ],
    [
        r"what is the role of engineers in sustainable agriculture ?",
        ["Engineers contribute to sustainable agriculture by designing precision farming technologies, developing efficient irrigation systems, creating agricultural machinery, and promoting eco-friendly farming practices."]
    ],
    [
        r"how is engineering being applied in the renewable energy sector ?",
        ["Engineering is being applied in the renewable energy sector through the design and development of solar panels, wind turbines, hydropower systems, bioenergy technologies, and energy storage solutions."]
    ],
    [
        r"what are the opportunities for engineers in the field of robotics ?",
        ["Opportunities for engineers in the field of robotics include designing and developing robots for various industries, such as manufacturing, healthcare, agriculture, exploration, and assisting in research and development."]
    ],
    [
        r"what is the role of engineering in disaster recovery ?",
        ["Engineering plays a vital role in disaster recovery by assessing damage, designing and implementing reconstruction plans, restoring infrastructure, and ensuring resilient systems for future resilience."]
    ],
    [
        r"what are the challenges in developing sustainable transportation systems ?",
        ["Challenges in developing sustainable transportation systems include infrastructure requirements, adoption of clean energy sources, public acceptance, cost-effectiveness, and integration of emerging technologies."]
    ],
    [
        r"what is the role of engineers in space exploration ?",
        ["Engineers contribute to space exploration by designing spacecraft, developing propulsion systems, creating life support systems, designing scientific instruments, and solving unique engineering challenges related to space missions."]
    ],
    [
        r"how is engineering being applied in the field of medicine ?",
        ["Engineering is being applied in the field of medicine through the development of medical devices, imaging technologies, prosthetics, tissue engineering, drug delivery systems, and advanced diagnostic tools."]
    ],
    [
        r"what is the role of engineering in the development of smart grids ?",
        ["Engineering plays a crucial role in the development of smart grids by designing and implementing advanced power distribution systems, integrating renewable energy sources, enabling two-way communication, and optimizing energy management."]
    ],
    [
        r"what is the role of engineers in the aerospace industry ?",
        ["Engineers play a crucial role in the aerospace industry by designing and developing aircraft, spacecraft, satellites, propulsion systems, navigation systems, and ensuring safety and efficiency in aviation and space exploration."]
    ],
    [
        r"what is the impact of engineering on the healthcare industry ?",
        ["Engineering has a significant impact on the healthcare industry through the development of medical devices, advancements in imaging technologies, improved diagnostic tools, robotic surgery systems, and telemedicine solutions."]
    ],
    [
        r"what is the role of engineers in sustainable urban planning ?",
        ["Engineers contribute to sustainable urban planning by designing efficient transportation systems, implementing green infrastructure, developing smart city technologies, promoting sustainable construction practices, and addressing environmental and social challenges."]
    ],
    [
        r"what is the role of engineering in the development of renewable energy technologies ?",
        ["Engineering plays a vital role in the development of renewable energy technologies by designing and optimizing solar panels, wind turbines, hydroelectric power systems, geothermal systems, and energy storage solutions."]
    ],
    [
        r"what are the ethical considerations in the development of autonomous vehicles ?",
        ["Ethical considerations in the development of autonomous vehicles include safety, liability, decision-making algorithms, privacy concerns, and the impact on jobs and society."]
    ],
    [
        r"how is engineering being applied in the field of artificial intelligence ?",
        ["Engineering is being applied in the field of artificial intelligence through the development of machine learning algorithms, neural networks, natural language processing systems, and intelligent automation solutions."]
    ],
    [
        r"what is the role of engineers in sustainable waste management ?",
        ["Engineers play a significant role in sustainable waste management by designing efficient waste disposal systems, developing recycling technologies, implementing waste-to-energy solutions, and promoting circular economy principles."]
    ],
    [
        r"what are the challenges in developing sustainable infrastructure ?",
        ["Challenges in developing sustainable infrastructure include balancing economic and environmental concerns, ensuring long-term durability, integrating renewable energy sources, addressing climate change impacts, and considering social and cultural factors."]
    ],
    [
        r"what is the role of engineers in the development of clean water technologies ?",
        ["Engineers contribute to the development of clean water technologies by designing water treatment systems, developing desalination technologies, implementing efficient water distribution networks, and addressing water pollution challenges."]
    ],
    [
        r"what is the impact of engineering on the telecommunications industry ?",
        ["Engineering has a significant impact on the telecommunications industry through the design and development of communication networks, mobile technologies, satellite systems, fiber optics, and data transmission technologies."]
    ],
    [
        r"what is the role of engineers in the development of sustainable materials ?",
        ["Engineers play a crucial role in the development of sustainable materials by designing eco-friendly alternatives, improving material efficiency, reducing waste, and optimizing material properties for various applications."]
    ],
    [
        r"what are the opportunities for engineers in the field of renewable energy ?",
        ["Opportunities for engineers in the field of renewable energy include designing and developing solar power systems, wind farms, hydroelectric plants, bioenergy projects, energy storage solutions, and optimizing renewable energy integration."]
    ],
    [
        r"what is the role of engineers in the development of smart healthcare technologies ?",
        ["Engineers contribute to the development of smart healthcare technologies by designing wearable devices, remote monitoring systems, telemedicine platforms, health informatics solutions, and personalized healthcare applications."]
    ],
    
]
        


def get_response(user_input):
    for pattern, response in pairs:
        if pattern.lower() in user_input.lower():
            return response
    return "I'm sorry, but I don't have a response for that."

# Streamlit app
def main():
    st.title("Engineering Chatbot")

    user_input = st.text_input("User Input")

    if st.button("Submit"):
        if user_input:
            response = get_response(user_input)
            st.text_area("Chatbot Response", response)
        else:
            st.warning("Please enter a valid input.")

if __name__ == "__main__":
    main()
