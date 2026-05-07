#!/usr/bin/env python3
"""Replace MODULES + QUESTIONS block in courses/claude-api/index.html."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "courses" / "claude-api" / "index.html"

NEW_BLOCK = r'''
    const MODULES = {
      intro:    { en: "Introduction & overview", vi: "Giới thiệu & tổng quan" },
      api:      { en: "Accessing Claude with the API", vi: "Truy cập Claude qua API" },
      control:  { en: "System prompts, streaming & structured output", vi: "System prompt, streaming & đầu ra có cấu trúc" },
      eval:     { en: "Prompt evaluation", vi: "Đánh giá prompt (eval)" },
      pengine:  { en: "Prompt engineering techniques", vi: "Kỹ thuật prompt engineering" },
      tools:    { en: "Tool use with Claude", vi: "Tool use với Claude" },
      rag:      { en: "RAG & agentic search", vi: "RAG & tìm kiếm agentic" },
      features: { en: "Features of Claude", vi: "Tính năng của Claude" },
      mcp:      { en: "Model Context Protocol", vi: "Model Context Protocol (MCP)" },
      apps:     { en: "Anthropic apps", vi: "Ứng dụng Anthropic" },
      agents:   { en: "Agents & workflows", vi: "Agent & workflow" },
      privacy:  { en: "Bonus · Data and privacy", vi: "Bổ sung · Dữ liệu & quyền riêng tư" }
    };

    const QUESTIONS = [
      { module: "intro",
        q: { en: "What is the main focus of “Building with the Claude API”?",
             vi: "Trọng tâm chính của khóa “Building with the Claude API” là gì?" },
        options: [
          { en: "Training foundation models from scratch on raw GPUs",
            vi: "Huấn luyện foundation model từ đầu trên GPU thô" },
          { en: "Teaching developers to integrate Claude into applications using the Anthropic API",
            vi: "Dạy developer tích hợp Claude vào ứng dụng qua Anthropic API",
            correct: true },
          { en: "Replacing Python with COBOL for all AI workloads",
            vi: "Thay Python bằng COBOL cho mọi workload AI" },
          { en: "Building only static websites without any backend",
            vi: "Chỉ xây website tĩnh, không backend" }
        ],
        explanation: {
          en: "The course focuses on API integration: authentication, conversations, tools, RAG, MCP, and production patterns for Claude-powered apps.",
          vi: "Khóa học tập trung vào tích hợp API: xác thực, hội thoại, tool, RAG, MCP và các pattern triển khai ứng dụng dùng Claude."
        }
      },
      { module: "api",
        q: { en: "How do you authenticate Anthropic API requests?",
             vi: "Bạn xác thực request Anthropic API như thế nào?" },
        options: [
          { en: "Paste your password in the JSON body field \"password\"",
            vi: "Dán mật khẩu vào JSON trong trường \"password\"" },
          { en: "Include an API key via the standard Anthropic headers / client configuration (never commit keys to source control)",
            vi: "Đưa API key qua header / cấu hình client chuẩn của Anthropic (không commit key vào mã nguồn)",
            correct: true },
          { en: "API requests require no authentication",
            vi: "Request API không cần xác thực" },
          { en: "Mail your API key to Anthropic support before each call",
            vi: "Gửi API key qua email cho Anthropic trước mỗi lần gọi" }
        ],
        explanation: {
          en: "Use API keys from the Anthropic Console with official SDKs or REST calls; manage keys securely (env vars, secret stores).",
          vi: "Dùng API key từ Anthropic Console với SDK hoặc REST; quản lý key an toàn (biến môi trường, secret store)."
        }
      },
      { module: "api",
        q: { en: "What does a multi-turn conversation look like in the Messages API?",
             vi: "Hội thoại nhiều lượt trong Messages API có dạng như thế nào?" },
        options: [
          { en: "A single user string with no history",
            vi: "Một chuỗi user duy nhất, không có lịch sử" },
          { en: "An ordered list of messages with roles such as user and assistant",
            vi: "Danh sách tin nhắn có thứ tự với vai trò như user và assistant",
            correct: true },
          { en: "Only assistant messages are allowed",
            vi: "Chỉ cho phép tin assistant" },
          { en: "Multi-turn is handled automatically without sending prior turns",
            vi: "Đa lượt được xử lý tự động mà không gửi lượt trước" }
        ],
        explanation: {
          en: "You send prior turns as structured messages so Claude maintains conversational context.",
          vi: "Bạn gửi các lượt trước dưới dạng message có cấu trúc để Claude giữ ngữ cảnh hội thoại."
        }
      },
      { module: "control",
        q: { en: "What is the primary purpose of a system prompt?",
             vi: "Mục đích chính của system prompt là gì?" },
        options: [
          { en: "Store end-user passwords",
            vi: "Lưu mật khẩu người dùng cuối" },
          { en: "Provide high-level instructions and constraints that shape assistant behavior across turns",
            vi: "Cung cấp chỉ dẫn và ràng buộc cấp cao định hình hành vi assistant qua các lượt",
            correct: true },
          { en: "Replace the need for any user messages",
            vi: "Thay thế hoàn toàn tin nhắn user" },
          { en: "Disable tool use entirely",
            vi: "Vô hiệu hóa hoàn toàn tool use" }
        ],
        explanation: {
          en: "System prompts set policies, tone, formatting rules, and safety guidance that persist across the conversation.",
          vi: "System prompt đặt chính sách, giọng điệu, quy tắc định dạng và hướng dẫn an toàn xuyên suốt hội thoại."
        }
      },
      { module: "control",
        q: { en: "What does increasing temperature generally do?",
             vi: "Tăng temperature thường làm gì?" },
        options: [
          { en: "Makes outputs more deterministic and repetitive",
            vi: "Làm đầu ra xác định hơn và lặp lại hơn" },
          { en: "Increases randomness / diversity of sampling (more creative, less deterministic)",
            vi: "Tăng độ ngẫu nhiên / đa dạng khi sampling (sáng tạo hơn, ít xác định hơn)",
            correct: true },
          { en: "Doubles your API quota automatically",
            vi: "Tự động gấp đôi quota API" },
          { en: "Turns off streaming",
            vi: "Tắt streaming" }
        ],
        explanation: {
          en: "Higher temperature increases variability in token sampling; lower temperature tends toward more focused, repeatable outputs.",
          vi: "Temperature cao hơn làm biến thiên sampling tăng; temperature thấp thường tập trung, lặp lại hơn."
        }
      },
      { module: "control",
        q: { en: "Why use response streaming?",
             vi: "Vì sao dùng streaming phản hồi?" },
        options: [
          { en: "To reduce model quality",
            vi: "Để giảm chất lượng model" },
          { en: "To deliver tokens incrementally for lower perceived latency and interactive UX",
            vi: "Để trả token dần, giảm độ trễ cảm nhận và UX tương tác",
            correct: true },
          { en: "Streaming is required for every API request",
            vi: "Mọi request API đều bắt buộc streaming" },
          { en: "Streaming disables tools",
            vi: "Streaming vô hiệu tool" }
        ],
        explanation: {
          en: "Streaming lets clients render partial responses while generation continues—great for chat UIs.",
          vi: "Streaming cho phép hiển thị phần trả lời trong khi model còn sinh token — rất hợp UI chat."
        }
      },
      { module: "control",
        q: { en: "What is structured output useful for?",
             vi: "Đầu ra có cấu trúc (structured output) hữu ích để làm gì?" },
        options: [
          { en: "Random unstructured prose only",
            vi: "Chỉ sinh văn xuôi không cấu trúc" },
          { en: "Returning machine-parseable data (e.g., JSON) that downstream code can validate and route",
            vi: "Trả dữ liệu máy có thể parse (ví dụ JSON) để code downstream kiểm tra và định tuyến",
            correct: true },
          { en: "Preventing multi-turn conversations",
            vi: "Ngăn hội thoại đa lượt" },
          { en: "Avoiding system prompts",
            vi: "Tránh system prompt" }
        ],
        explanation: {
          en: "Structured outputs integrate cleanly with databases, UIs, and automation—especially when paired with schemas or tools.",
          vi: "Đầu ra có cấu trúc tích hợp tốt với DB, UI và tự động hóa — đặc biệt khi kèm schema hoặc tool."
        }
      },
      { module: "eval",
        q: { en: "What is a common first step in prompt evaluation workflows?",
             vi: "Bước đầu phổ biến trong quy trình đánh giá prompt là gì?" },
        options: [
          { en: "Delete all logs",
            vi: "Xóa toàn bộ log" },
          { en: "Build or generate a test dataset that represents real tasks and edge cases",
            vi: "Xây hoặc sinh bộ dữ liệu test phản ánh tác vụ thực và edge case",
            correct: true },
          { en: "Disable monitoring in production",
            vi: "Tắt giám sát production" },
          { en: "Replace the model with a spreadsheet",
            vi: "Thay model bằng bảng tính" }
        ],
        explanation: {
          en: "Evaluations rely on representative tasks (often synthetic + curated) to measure changes reliably.",
          vi: "Eval cần tập tác vụ đại diện (thường tổng hợp + chọn lọc) để đo thay đổi đáng tin."
        }
      },
      { module: "eval",
        q: { en: "What is model-based grading?",
             vi: "Model-based grading là gì?" },
        options: [
          { en: "Humans always vote without any criteria",
            vi: "Con người luôn bỏ phiếu không tiêu chí" },
          { en: "Using a model (often with a rubric) to score outputs at scale as part of an eval pipeline",
            vi: "Dùng model (thường kèm rubric) để chấm điểm đầu ra quy mô lớn trong pipeline eval",
            correct: true },
          { en: "Randomly assigning scores",
            vi: "Gán điểm ngẫu nhiên" },
          { en: "Deleting incorrect answers silently",
            vi: "Xóa âm thầm câu sai" }
        ],
        explanation: {
          en: "Model grading automates scoring but still needs careful rubrics, spot checks, and bias awareness.",
          vi: "Chấm bằng model giúp tự động hóa nhưng vẫn cần rubric kỹ, kiểm tra chéo và lưu ý thiên kiến."
        }
      },
      { module: "pengine",
        q: { en: "Why structure prompts with XML-like tags?",
             vi: "Vì sao dùng thẻ kiểu XML để cấu trúc prompt?" },
        options: [
          { en: "XML tags make prompts slower with no benefit",
            vi: "Thẻ XML làm prompt chậm mà không lợi" },
          { en: "They separate instructions, context, and examples so the model can follow each part reliably",
            vi: "Tách chỉ dẫn, ngữ cảnh và ví dụ để model bám theo từng phần ổn định hơn",
            correct: true },
          { en: "XML tags are forbidden by the API",
            vi: "API cấm dùng thẻ XML" },
          { en: "Tags remove the need for user messages",
            vi: "Thẻ loại bỏ hoàn toàn tin user" }
        ],
        explanation: {
          en: "Tagged sections reduce ambiguity and improve consistency—especially for complex prompts.",
          vi: "Phần được gắn thẻ giảm mơ hồ và tăng nhất quán — đặc biệt với prompt phức tạp."
        }
      },
      { module: "pengine",
        q: { en: "How do concrete examples in prompts help?",
             vi: "Ví dụ cụ thể trong prompt giúp gì?" },
        options: [
          { en: "They confuse the model",
            vi: "Chúng làm model bối rối" },
          { en: "They demonstrate the desired format and behavior (few-shot style guidance)",
            vi: "Chúng minh họa định dạng và hành vi mong muốn (few-shot)",
            correct: true },
          { en: "Examples disable tools automatically",
            vi: "Ví dụ tự động tắt tool" },
          { en: "Examples must be longer than 50 pages",
            vi: "Ví dụ phải dài hơn 50 trang" }
        ],
        explanation: {
          en: "Examples anchor patterns: tone, structure, edge-case handling, and output formatting.",
          vi: "Ví dụ neo pattern: giọng điệu, cấu trúc, xử lý edge case và định dạng đầu ra."
        }
      },
      { module: "tools",
        q: { en: "What must tool definitions include for tool use?",
             vi: "Định nghĩa tool cho tool use phải có gì?" },
        options: [
          { en: "Only the tool name—parameters are forbidden",
            vi: "Chỉ tên tool — cấm tham số" },
          { en: "A clear schema for inputs (parameters) so Claude can call tools safely and consistently",
            vi: "Schema rõ ràng cho đầu vào (tham số) để Claude gọi tool an toàn và nhất quán",
            correct: true },
          { en: "Your database password",
            vi: "Mật khẩu cơ sở dữ liệu" },
          { en: "Random Unicode characters only",
            vi: "Chỉ ký tự Unicode ngẫu nhiên" }
        ],
        explanation: {
          en: "Schemas document expected arguments and types, enabling validation and fewer malformed calls.",
          vi: "Schema mô tả tham số và kiểu, hỗ trợ validate và giảm lỗi gọi."
        }
      },
      { module: "tools",
        q: { en: "After Claude requests a tool call, what does your application typically do next?",
             vi: "Sau khi Claude yêu cầu gọi tool, ứng dụng của bạn thường làm gì tiếp?" },
        options: [
          { en: "Ignore the tool call and stop",
            vi: "Bỏ qua tool call và dừng" },
          { en: "Execute the tool, then return tool results to Claude so it can continue reasoning",
            vi: "Chạy tool, rồi trả kết quả tool cho Claude để tiếp tục suy luận",
            correct: true },
          { en: "Delete the conversation history permanently",
            vi: "Xóa vĩnh viễn lịch sử hội thoại" },
          { en: "Ask the user to reboot the server",
            vi: "Bảo user khởi động lại máy chủ" }
        ],
        explanation: {
          en: "Tool use is multi-step: model proposes tool calls → host executes → results go back as tool_result blocks.",
          vi: "Tool use nhiều bước: model đề xuất → host thực thi → kết quả trả về dưới dạng tool_result."
        }
      },
      { module: "tools",
        q: { en: "Which capability extends Claude with live web retrieval in supported setups?",
             vi: "Khả năng nào mở rộng Claude với tra cứu web trực tiếp trong các thiết lập được hỗ trợ?" },
        options: [
          { en: "Printing to a fax machine",
            vi: "In ra máy fax" },
          { en: "Web search tooling that lets Claude fetch up-to-date information when enabled",
            vi: "Công cụ web search cho Claude lấy thông tin cập nhật khi được bật",
            correct: true },
          { en: "Disabling HTTPS",
            vi: "Tắt HTTPS" },
          { en: "Replacing JSON with XML everywhere",
            vi: "Thay JSON bằng XML mọi nơi" }
        ],
        explanation: {
          en: "Web search is presented as a tool in product/API flows where enabled—great for fresh facts with citations when available.",
          vi: "Web search là một tool trong luồng API/sản phẩm khi bật — hữu ích cho thông tin mới và trích dẫn."
        }
      },
      { module: "rag",
        q: { en: "Why chunk documents for RAG?",
             vi: "Vì sao cần chunk tài liệu cho RAG?" },
        options: [
          { en: "Chunking always deletes half the document",
            vi: "Chunk luôn xóa nửa tài liệu" },
          { en: "To create retrievable units that fit embedding/context limits and improve recall precision",
            vi: "Tạo đơn vị truy vấn vừa giới hạn embedding/ngữ cảnh và cải thiện độ chính xác recall",
            correct: true },
          { en: "Chunks must be exactly one token",
            vi: "Chunk phải đúng một token" },
          { en: "RAG never uses chunks",
            vi: "RAG không bao giờ dùng chunk" }
        ],
        explanation: {
          en: "Chunking strategy affects what gets retrieved—overlap, boundaries, and metadata matter.",
          vi: "Chiến lược chunk ảnh hưởng phần được truy xuất — overlap, ranh giới và metadata đều quan trọng."
        }
      },
      { module: "rag",
        q: { en: "What role do text embeddings play in many RAG pipelines?",
             vi: "Embedding văn bản đóng vai trò gì trong nhiều pipeline RAG?" },
        options: [
          { en: "They compress images only",
            vi: "Chỉ nén ảnh" },
          { en: "They represent text meaningfully for semantic similarity search against a vector index",
            vi: "Biểu diễn ngữ nghĩa để tìm kiếm tương đồng ngữ nghĩa trên vector index",
            correct: true },
          { en: "They replace the need for any retrieval step",
            vi: "Thay thế hoàn toàn bước retrieval" },
          { en: "Embeddings are incompatible with Claude",
            vi: "Embedding không tương thích Claude" }
        ],
        explanation: {
          en: "Embeddings enable semantic retrieval; often paired with chunk metadata and re-ranking.",
          vi: "Embedding cho phép retrieval ngữ nghĩa; thường kèm metadata chunk và re-rank."
        }
      },
      { module: "rag",
        q: { en: "What does BM25 primarily implement?",
             vi: "BM25 chủ yếu thực hiện điều gì?" },
        options: [
          { en: "Neural image generation",
            vi: "Sinh ảnh neural" },
          { en: "Lexical (keyword) scoring often used in hybrid search setups",
            vi: "Điểm từ vựng (keyword) thường dùng trong tìm kiếm hybrid",
            correct: true },
          { en: "GPU thermal management",
            vi: "Quản lý nhiệt GPU" },
          { en: "PDF rendering",
            vi: "Render PDF" }
        ],
        explanation: {
          en: "BM25 is great for exact token matches; hybrid pipelines combine BM25 with dense retrieval for robustness.",
          vi: "BM25 mạnh với khớp từ khóa; pipeline hybrid kết hợp BM25 + dense retrieval cho bền vững hơn."
        }
      },
      { module: "rag",
        q: { en: "What is the core idea of retrieval-augmented generation (RAG)?",
             vi: "Ý tưởng cốt lõi của RAG là gì?" },
        options: [
          { en: "Never retrieve anything—only hallucinate",
            vi: "Không retrieve — chỉ hallucinate" },
          { en: "Retrieve relevant context first, then generate an answer grounded in that context",
            vi: "Retrieve ngữ cảnh liên quan trước, rồi sinh câu trả lời dựa trên đó",
            correct: true },
          { en: "Always fine-tune the base model on every request",
            vi: "Luôn fine-tune base model mỗi request" },
          { en: "Require offline-only inference",
            vi: "Bắt buộc suy luận chỉ offline" }
        ],
        explanation: {
          en: "RAG improves factual grounding by conditioning generation on retrieved documents or snippets.",
          vi: "RAG cải thiện neo fact bằng cách điều kiện hóa sinh trên tài liệu/snippet đã retrieve."
        }
      },
      { module: "features",
        q: { en: "What is extended thinking mode primarily for?",
             vi: "Chế độ extended thinking chủ yếu dùng để làm gì?" },
        options: [
          { en: "Skips reasoning entirely",
            vi: "Bỏ qua hoàn toàn suy luận" },
          { en: "Allocates additional reasoning effort before producing the final answer (where supported)",
            vi: "Thêm nỗ lực suy luận trước khi đưa ra câu trả lời cuối (nơi được hỗ trợ)",
            correct: true },
          { en: "Disables citations",
            vi: "Tắt trích dẫn" },
          { en: "Requires fax integration",
            vi: "Bắt buộc tích hợp fax" }
        ],
        explanation: {
          en: "Extended thinking helps on harder tasks by splitting internal reasoning from the user-visible answer.",
          vi: "Extended thinking giúp tác vụ khó bằng cách tách suy luận nội bộ và phần trả lời hiển thị."
        }
      },
      { module: "features",
        q: { en: "Which multimodal inputs does the API ecosystem commonly emphasize in this course?",
             vi: "Khóa học thường nhấn mạnh đầu vào đa phương thức nào trong hệ sinh thái API?" },
        options: [
          { en: "Only MIDI music files",
            vi: "Chỉ file MIDI" },
          { en: "Images (vision) and PDF/document workflows alongside text",
            vi: "Ảnh (vision) và luồng PDF/tài liệu cùng văn bản",
            correct: true },
          { en: "Only punch cards",
            vi: "Chỉ thẻ đục lỗ" },
          { en: "VR headset telemetry only",
            vi: "Chỉ dữ liệu headset VR" }
        ],
        explanation: {
          en: "Multimodal APIs combine text with images/PDFs for richer automation (analysis, extraction, summarization).",
          vi: "API đa phương thức kết hợp text với ảnh/PDF để tự động hóa phong phú hơn."
        }
      },
      { module: "features",
        q: { en: "What is a major benefit of prompt caching?",
             vi: "Lợi ích chính của prompt caching là gì?" },
        options: [
          { en: "It guarantees perfect accuracy",
            vi: "Đảm bảo độ chính xác tuyệt đối" },
          { en: "It can reduce latency and cost by reusing stable prompt prefixes across requests",
            vi: "Giảm độ trễ và chi phí bằng cách tái sử dụng prefix prompt ổn định giữa các request",
            correct: true },
          { en: "It deletes user data automatically",
            vi: "Tự động xóa dữ liệu user" },
          { en: "It removes the need for tools",
            vi: "Loại bỏ nhu cầu tool" }
        ],
        explanation: {
          en: "Caching helps when large system prompts or repeated documents form a stable prefix.",
          vi: "Caching hữu ích khi system prompt lớn hoặc tài liệu lặp lại tạo prefix ổn định."
        }
      },
      { module: "mcp",
        q: { en: "What problem does the Model Context Protocol (MCP) address?",
             vi: "Model Context Protocol (MCP) giải quyết vấn đề gì?" },
        options: [
          { en: "Printing receipts",
            vi: "In biên lai" },
          { en: "Standardizing how applications expose tools, resources, and prompts to models and clients",
            vi: "Chuẩn hóa cách ứng dụng expose tool, resource và prompt cho model và client",
            correct: true },
          { en: "Replacing HTTP entirely",
            vi: "Thay thế hoàn toàn HTTP" },
          { en: "Banning embeddings",
            vi: "Cấm embedding" }
        ],
        explanation: {
          en: "MCP helps build interoperable integrations—think composable tool servers and consistent client patterns.",
          vi: "MCP giúp tích hợp tương tác — server tool có thể kết hợp và pattern client nhất quán."
        }
      },
      { module: "mcp",
        q: { en: "Besides tools, what else can MCP servers expose?",
             vi: "Ngoài tools, MCP server còn có thể expose gì?" },
        options: [
          { en: "Nothing else—tools only",
            vi: "Không gì khác — chỉ tools" },
          { en: "Resources (like readable content) and prompts that clients can discover and use",
            vi: "Resource (nội dung đọc được) và prompt mà client có thể khám phá và dùng",
            correct: true },
          { en: "Physical hardware warranties",
            vi: "Bảo hành phần cứng vật lý" },
          { en: "Company payroll databases without auth",
            vi: "DB lương công ty không cần auth" }
        ],
        explanation: {
          en: "MCP's ecosystem includes tools, resources, and prompts—making integrations more discoverable.",
          vi: "Hệ sinh thái MCP gồm tools, resources và prompts — giúp tích hợp dễ khám phá hơn."
        }
      },
      { module: "apps",
        q: { en: "What is Claude Code aimed at?",
             vi: "Claude Code hướng tới điều gì?" },
        options: [
          { en: "Replacing Windows kernel development only",
            vi: "Chỉ thay thế phát triển kernel Windows" },
          { en: "Developer workflows like autonomous coding assistance integrated into development environments",
            vi: "Luồng dev như trợ lý lập trình tích hợp môi trường phát triển",
            correct: true },
          { en: "Running COBOL mainframes only",
            vi: "Chỉ chạy mainframe COBOL" },
          { en: "Designing printed brochures",
            vi: "Thiết kế brochure in ấn" }
        ],
        explanation: {
          en: "Claude Code focuses on AI-assisted software engineering tasks with tooling integrations.",
          vi: "Claude Code tập trung tác vụ kỹ sư phần mềm có AI trợ giúp và tích hợp công cụ."
        }
      },
      { module: "apps",
        q: { en: "What does Computer Use typically enable?",
             vi: "Computer Use thường cho phép điều gì?" },
        options: [
          { en: "Formatting floppy disks only",
            vi: "Chỉ format đĩa mềm" },
          { en: "Automating interactions with a computer interface for tasks like UI-driven workflows",
            vi: "Tự động hóa tương tác giao diện máy tính cho luồng kiểu UI",
            correct: true },
          { en: "Guaranteed bug-free software",
            vi: "Đảm bảo phần mềm không lỗi" },
          { en: "Offline-only batch compilation",
            vi: "Chỉ biên dịch batch offline" }
        ],
        explanation: {
          en: "Computer Use targets GUI automation scenarios—powerful but requiring careful safety constraints.",
          vi: "Computer Use nhắm tự động hóa GUI — mạnh nhưng cần ràng buộc an toàn cẩn thận."
        }
      },
      { module: "agents",
        q: { en: "Which workflow pattern runs multiple independent tasks concurrently to reduce wall-clock time?",
             vi: "Pattern workflow nào chạy nhiều tác vụ độc lập đồng thời để giảm thời gian thực tế?" },
        options: [
          { en: "Routing",
            vi: "Routing" },
          { en: "Parallelization",
            vi: "Song song hóa (parallelization)",
            correct: true },
          { en: "Chaining only",
            vi: "Chỉ chaining" },
          { en: "Single-threaded sequential only",
            vi: "Chỉ tuần tự một luồng" }
        ],
        explanation: {
          en: "Parallelization trades orchestration complexity for throughput when tasks are independent.",
          vi: "Parallelization đánh đổi độ phức tạp điều phối lấy throughput khi tác vụ độc lập."
        }
      },
      { module: "agents",
        q: { en: "What is routing in agent workflows?",
             vi: "Routing trong workflow agent là gì?" },
        options: [
          { en: "Always executing every branch every time",
            vi: "Luôn chạy mọi nhánh mọi lúc" },
          { en: "Choosing which specialized path or model handles an input based on classification or rules",
            vi: "Chọn đường/chuyên gia hoặc model xử lý đầu vào dựa trên phân loại hoặc rule",
            correct: true },
          { en: "Deleting logs",
            vi: "Xóa log" },
          { en: "Replacing IPv4 with IPv6 automatically",
            vi: "Tự thay IPv4 bằng IPv6" }
        ],
        explanation: {
          en: "Routing improves quality/cost by sending easy tasks to smaller models and hard tasks to stronger ones.",
          vi: "Routing cải thiện chất lượng/chi phí bằng cách gửi tác vụ dễ tới model nhỏ, tác vụ khó tới model mạnh hơn."
        }
      },

      { module: "privacy",
        q: { en: "What is Skilljar in this context?",
             vi: "Trong bối cảnh này, Skilljar là gì?" },
        options: [
          { en: "A learning management system that hosts the course content",
            vi: "Một LMS lưu trữ nội dung khóa học",
            correct: true },
          { en: "A Claude model variant",
            vi: "Biến thể model Claude" },
          { en: "Anthropic's on-prem database product",
            vi: "Sản phẩm CSDL on-prem của Anthropic" },
          { en: "A Kubernetes distribution",
            vi: "Bản phân phối Kubernetes" }
        ],
        explanation: {
          en: "Skilljar is the LMS that hosts Anthropic Academy courses and tracks progress.",
          vi: "Skilljar là LMS lưu khóa Anthropic Academy và theo dõi tiến độ."
        }
      },
      { module: "privacy",
        q: { en: "Which data does Skilljar collect about your learning activity?",
             vi: "Skilljar thu thập dữ liệu gì về hoạt động học?" },
        options: [
          { en: "Course progress, lesson completion, quiz scores, and time spent",
            vi: "Tiến độ khóa học, hoàn thành bài, điểm quiz và thời gian học",
            correct: true },
          { en: "Your debit card PIN",
            vi: "Mã PIN thẻ ghi nợ" },
          { en: "Full contents of your private git repos",
            vi: "Toàn bộ nội dung repo git riêng" },
          { en: "Nothing at all",
            vi: "Không gì cả" }
        ],
        explanation: {
          en: "Skilljar collects basic learning analytics such as progress, completion, quiz scores, and time on materials.",
          vi: "Skilljar thu thập phân tích học tập cơ bản: tiến độ, hoàn thành, điểm quiz, thời gian học."
        }
      },
      { module: "privacy",
        q: { en: "How is Skilljar data different from your Anthropic account data?",
             vi: "Dữ liệu Skilljar khác gì so với tài khoản Anthropic?" },
        options: [
          { en: "Skilljar tracks course progress; Anthropic accounts manage Console / Claude AI service access",
            vi: "Skilljar theo dõi tiến độ khóa; tài khoản Anthropic quản lý truy cập Console / Claude AI",
            correct: true },
          { en: "They are identical in every way",
            vi: "Giống hệt mọi mặt" },
          { en: "Skilljar stores your production API traffic logs by default",
            vi: "Skilljar mặc định lưu log traffic API production của bạn" },
          { en: "Anthropic accounts cannot use APIs",
            vi: "Tài khoản Anthropic không dùng được API" }
        ],
        explanation: {
          en: "Learning progress on Skilljar is separate from product accounts used for API and Claude services.",
          vi: "Tiến độ học trên Skilljar tách biệt tài khoản sản phẩm dùng cho API và dịch vụ Claude."
        }
      },
      { module: "privacy",
        q: { en: "Which best describes Skilljar's security posture?",
             vi: "Mô tả nào đúng nhất về bảo mật của Skilljar?" },
        options: [
          { en: "No encryption, no audits",
            vi: "Không mã hóa, không kiểm tra" },
          { en: "Industry-standard security including encryption, secure hosting, audits, and SOC 2 compliance",
            vi: "Bảo mật chuẩn ngành gồm mã hóa, lưu trữ an toàn, kiểm tra và tuân thủ SOC 2",
            correct: true },
          { en: "Customer data is posted publicly by default",
            vi: "Dữ liệu khách hàng công khai mặc định" },
          { en: "SOC 2 forbids any cloud hosting",
            vi: "SOC 2 cấm mọi cloud hosting" }
        ],
        explanation: {
          en: "Skilljar states it follows strong security practices including SOC 2 compliance.",
          vi: "Skilljar nêu rõ tuân thủ thực hành bảo mật mạnh, gồm SOC 2."
        }
      },
      { module: "privacy",
        q: { en: "How do you request deletion of your learning data or Skilljar account?",
             vi: "Làm sao để yêu cầu xóa dữ liệu học hoặc tài khoản Skilljar?" },
        options: [
          { en: "Email academy-support@anthropic.com",
            vi: "Gửi email tới academy-support@anthropic.com",
            correct: true },
          { en: "Tweet publicly with your API key",
            vi: "Tweet công khai kèm API key" },
          { en: "It cannot be deleted ever",
            vi: "Không thể xóa vĩnh viễn" },
          { en: "Delete via DNS configuration",
            vi: "Xóa qua cấu hình DNS" }
        ],
        explanation: {
          en: "Deletion requests go to academy-support@anthropic.com and are handled under privacy and retention policies.",
          vi: "Yêu cầu xóa gửi tới academy-support@anthropic.com theo chính sách quyền riêng tư và lưu giữ."
        }
      },
      { module: "privacy",
        q: { en: "Do you need an Anthropic account only to watch Anthropic Academy courses on Skilljar?",
             vi: "Bạn có cần tài khoản Anthropic chỉ để xem khóa Anthropic Academy trên Skilljar không?" },
        options: [
          { en: "No — a Skilljar account is enough for course access; Anthropic accounts are for Console / Claude services",
            vi: "Không — chỉ cần tài khoản Skilljar để vào khóa; tài khoản Anthropic dùng cho Console / dịch vụ Claude",
            correct: true },
          { en: "Yes — Anthropic account is always mandatory",
            vi: "Có — luôn bắt buộc tài khoản Anthropic" },
          { en: "You must purchase Claude Max first",
            vi: "Phải mua Claude Max trước" },
          { en: "GitHub OAuth is the only login method",
            vi: "Chỉ đăng nhập GitHub OAuth" }
        ],
        explanation: {
          en: "Skilljar hosts the learning experience; using Claude products generally requires separate Anthropic credentials.",
          vi: "Skilljar host trải nghiệm học; dùng sản phẩm Claude thường cần thông tin đăng nhập Anthropic riêng."
        }
      }
    ];
'''

def main():
    text = HTML.read_text(encoding="utf-8")
    start = text.index("    const MODULES = {")
    end = text.index("\n    const quizEl", start)
    text = text[:start] + NEW_BLOCK + text[end:]
    HTML.write_text(text, encoding="utf-8")
    print(f"Updated {HTML} ({start}-{end} replaced)")


if __name__ == "__main__":
    main()
