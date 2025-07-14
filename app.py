from agentic_doc.parse import parse
from agentic_doc.connectors import LocalConnectorConfig
from agentic_doc.utils import viz_parsed_document
from agentic_doc.config import VisualizationConfig
from agentic_doc.common import ChunkType


# REFERENCE: https://github.com/landing-ai/agentic-doc 

config = LocalConnectorConfig()
doc_path = "analyst_reports"

# Parse all supported documents in a directory
# results = parse(config, connector_path=path_to_documents)

# Parse with pattern filtering
# results = parse(config, connector_path=path_to_documents, connector_pattern="*.pdf")

# Parse all supported documents in a directory recursively (search subdirectories as well)
config = LocalConnectorConfig(recursive=True)
results = parse(config, 
                connector_path=doc_path, 
                result_save_dir="results",
                grounding_save_dir="grounding")
print(f"Final result: {results[0].result_path}")
parsed_doc = results[0]

# add visualizations
# This did not work, getting a weird error 
'''
Traceback (most recent call last):
  File "/Users/sanshan/develop/code/github-repos-hellosantosh/llms-in-finance-project/app.py", line 42, in <module>
    images = viz_parsed_document(
             ^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.12/site-packages/agentic_doc/utils.py", line 307, in viz_parsed_document
    img = _read_img_rgb(str(file_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.12/site-packages/agentic_doc/utils.py", line 423, in _read_img_rgb
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
cv2.error: OpenCV(4.12.0) /Users/xperience/GHA-Actions-OpenCV/_work/opencv-python/opencv-python/opencv/modules/imgproc/src/color.cpp:199: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'
'''
'''
viz_config = VisualizationConfig(
    thickness=2,  # Thicker bounding boxes
    text_bg_opacity=0.8,  # More opaque text background
    font_scale=0.7,  # Larger text
    # Custom colors for different chunk types
    color_map={
        ChunkType.marginalia: (0,255,0),  # Green for marginalia
        ChunkType.table: (0, 0, 255),  # Red for tables
        ChunkType.figure: (255, 165, 0),  # Light blue for figures
        ChunkType.text: (255, 0, 0),  # Blue for regular text
    }
)

images = viz_parsed_document(
    doc_path,
    parsed_doc,
    output_dir = "visualizations",
    viz_config=viz_config
)
'''
