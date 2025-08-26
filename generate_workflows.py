import json
import uuid

def generate_workflows(count):
    workflows = []
    for i in range(count):
        workflow_id = str(uuid.uuid4())
        node_id = str(uuid.uuid4())
        workflows.append({
            "id": workflow_id,
            "name": f"Workflow {i+1}",
            "active": False,
            "nodes": [
                {
                    "parameters": {},
                    "id": node_id,
                    "name": "Start",
                    "type": "n8n-nodes-base.start",
                    "typeVersion": 1,
                    "position": [
                        250,
                        300
                    ]
                }
            ],
            "connections": {},
            "createdAt": "2024-05-14T12:00:00.000Z",
            "updatedAt": "2024-05-14T12:00:00.000Z",
            "settings": {},
            "staticData": None
        })
    return workflows

if __name__ == "__main__":
    workflows_data = generate_workflows(2000)
    with open("workflows.json", "w") as f:
        json.dump(workflows_data, f, indent=2)
    print("Generated 2000 workflows in workflows.json")
