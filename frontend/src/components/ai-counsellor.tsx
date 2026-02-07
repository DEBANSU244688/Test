"use client";

import { useState } from "react";

type ChatMessage = {
  role: "user" | "assistant";
  text: string;
};

export function AICounsellor() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    { role: "assistant", text: "Hi! I’m your AI career counsellor. What role are you targeting?" }
  ]);
  const [input, setInput] = useState("");

  function sendMessage() {
    if (!input.trim()) return;

    const userMessage: ChatMessage = { role: "user", text: input.trim() };
    const botMessage: ChatMessage = {
      role: "assistant",
      text: "Nice direction. Start with one weekly project milestone and one interview prep goal."
    };

    setMessages((prev) => [...prev, userMessage, botMessage]);
    setInput("");
  }

  return (
    <section className="grid gap-4 rounded-xl border border-slate-700 bg-surface p-6 md:grid-cols-[2fr_1fr]">
      <div>
        <h3 className="text-lg font-semibold">AI Career Counsellor</h3>
        <div className="mt-3 max-h-64 space-y-2 overflow-y-auto rounded-md border border-slate-600 bg-background p-3">
          {messages.map((message, index) => (
            <p
              key={`${message.role}-${index}`}
              className={`rounded-md px-3 py-2 text-sm ${message.role === "assistant" ? "bg-slate-800 text-slate-100" : "bg-primary/20 text-white"}`}
            >
              <span className="font-semibold">{message.role === "assistant" ? "Mentor" : "You"}:</span> {message.text}
            </p>
          ))}
        </div>

        <div className="mt-3 flex gap-2">
          <input
            className="w-full rounded-md border border-slate-600 bg-background px-3 py-2 text-sm"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask for learning advice..."
          />
          <button className="rounded-md bg-primary px-4 py-2 font-semibold text-slate-950" onClick={sendMessage} type="button">
            Send
          </button>
        </div>
      </div>

      <aside className="rounded-md border border-slate-600 bg-background p-3 text-sm text-slate-300">
        <p className="font-semibold text-white">Contextual insights</p>
        <ul className="mt-2 list-disc space-y-1 pl-4">
          <li>Target role alignment: Backend / Full-stack</li>
          <li>High-impact gap: System Design</li>
          <li>Suggested weekly focus: 1 project + 1 mock interview</li>
        </ul>
      </aside>
    </section>
  );
}
