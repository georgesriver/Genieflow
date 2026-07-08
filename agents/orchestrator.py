class Orchestrator:
    def __init__(self):
        self.state = "IDLE"
        self.journal = []

    def transition(self, new_state, data=None):
        print(f"[Log] Transitioning: {self.state} -> {new_state}")
        self.state = new_state
        if data:
            self.journal.append({"state": new_state, "data": data})

    def run_workflow(self, input_data, guardian):
        # 状态机逻辑
        self.transition("EXTRACTING")
        # 这里模拟提取过程
        extracted_data = f"Structured: {input_data}" 
        
        self.transition("VERIFYING", extracted_data)
        result = guardian.verify(extracted_data)
        
        self.transition("COMPLETED")
        return result

