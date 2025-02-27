import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

# Create Flask app
app = Flask(__name__)

# Base URLs for documentation (you can extend this dictionary with more paths if needed)
documentation_urls = {
    'Segment': 'https://segment.com/docs/getting-started/implementation-guide/',
    'mParticle': 'https://docs.mparticle.com/',
    'Lytics': 'https://docs.lytics.com/docs/developer-quickstart/',
    'Zeotap': 'https://docs.zeotap.com/'  # Update this URL if needed
}

# Map query keywords to relevant documentation sub-paths
query_to_subpath = {
    'setup': 'getting-started',
    'create': 'implementation-guide',
    'user profile': 'user-profile',
    'segment': 'audience-segments',
    'integration': 'integration-guide',
    
}

# Function to scrape the documentation content
def scrape_documentation(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')

        
        paragraphs = soup.find_all('p')
        content = " ".join([para.get_text() for para in paragraphs])
        return content
    except requests.exceptions.RequestException as e:
        return f"Error fetching data from the documentation: {str(e)}"

# Function to search documentation for a query
def search_documentation(query, platform=None):
    results = []
    query = query.lower().strip()  

    if platform:
      
        subpath = query_to_subpath.get(query, None)
        if subpath:
            url = documentation_urls[platform] + subpath
            content = scrape_documentation(url)
            if query in content.lower():
                snippet = content[:300] 
                results.append({
                    'platform': platform,
                    'snippet': snippet,
                    'full_content': content
                })
    else:
       
        for platform, url in documentation_urls.items():
            subpath = query_to_subpath.get(query, None)
            if subpath:
                full_url = url + subpath
                content = scrape_documentation(full_url)
                if query in content.lower():
                    snippet = content[:300]  
                    results.append({
                        'platform': platform,
                        'snippet': snippet,
                        'full_content': content
                    })

    return results

@app.route('/', methods=['GET', 'POST'])
def chatbot_view():
    if request.method == 'POST':
        query = request.form['query']
        platform = request.form.get('platform', None)  
        if query:
            
            results = search_documentation(query, platform)
            return jsonify({'results': results})

    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
