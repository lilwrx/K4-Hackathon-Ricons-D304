# Bảng kết quả chạy golden set

## Lượt chạy 1
- Mô tả: Prompting cơ bản, chưa có low-confidence routing và grounding chặt.
- Pass Rate: 60.0%
- Latency trung bình: 3.2s
- Kết quả: Không đạt quality bar.

## Lượt chạy 2
- Mô tả: Áp dụng BM25 context + strict system prompt.
- Pass Rate: 76.0%
- Latency trung bình: 2.1s
- Kết quả: Không đạt quality bar.

## Lượt chạy 3
- Mô tả: Tích hợp grounding filter + low-confidence routing.
- Pass Rate: 92.0%
- Latency trung bình: 1.8s
- Kết quả: Đạt quality bar.
